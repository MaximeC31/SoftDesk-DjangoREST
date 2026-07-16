from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Contributor, Project
from .serializers import ContributorSerializer, ProjectSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def project_collection_view(request):

    match request.method:
        case "GET":
            projects = (
                Project.objects.filter(
                    contributor__user=request.user,
                )
                .select_related("author")
                .order_by("-created_time")
            )

            paginator = PageNumberPagination()
            paginator.page_size = 10
            paginated_projects = paginator.paginate_queryset(projects, request)

            serializer = ProjectSerializer(paginated_projects, many=True)
            return paginator.get_paginated_response(serializer.data)

        case "POST":
            serializer = ProjectSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=400)

            project_instance = serializer.save(author=request.user)
            Contributor.objects.create(
                user=request.user,
                project=project_instance,
            )

            return Response(
                ProjectSerializer(project_instance).data,
                status=201,
            )


@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def project_detail_view(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=404)

    contributor = Contributor.objects.filter(
        user=request.user,
        project=project,
    ).first()
    if contributor is None:
        return Response(
            {"detail": "You are not a contributor to this project."},
            status=403,
        )

    match request.method:
        case "GET":
            return Response(ProjectSerializer(project).data, status=200)

        case "PATCH":
            if request.user != project.author:
                return Response(
                    {"detail": "You are not the author of this project."},
                    status=403,
                )

            serializer = ProjectSerializer(
                project,
                data=request.data,
                partial=True,
            )
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)

            serializer.save()
            return Response(serializer.data, status=200)

        case "DELETE":
            if request.user != project.author:
                return Response(
                    {"detail": "You are not the author of this project."},
                    status=403,
                )

            project.delete()
            return Response(status=204)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def project_contributors_collection_view(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=404)

    contributor = Contributor.objects.filter(
        user=request.user,
        project=project,
    ).first()
    if contributor is None:
        return Response(
            {"detail": "You are not a contributor to this project."},
            status=403,
        )

    match request.method:
        case "GET":
            contributors = (
                Contributor.objects.filter(project=project)
                .select_related("user")
                .order_by("-created_time")
            )
            paginator = PageNumberPagination()
            paginator.page_size = 10
            paginated_contributors = paginator.paginate_queryset(
                contributors,
                request,
            )
            serializer = ContributorSerializer(
                paginated_contributors,
                many=True,
            )
            return paginator.get_paginated_response(serializer.data)

        case "POST":
            if request.user != project.author:
                return Response(
                    {"detail": "You are not the author of this project."},
                    status=403,
                )

            serializer = ContributorSerializer(
                data=request.data,
                context={"project": project},
            )

            if not serializer.is_valid():
                return Response(serializer.errors, status=400)

            contributor = serializer.save()
            return Response(
                ContributorSerializer(contributor).data,
                status=201,
            )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def project_contributor_detail_view(request, project_id, contributor_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=404)

    if request.user != project.author:
        return Response(
            {"detail": "You are not the author of this project."},
            status=403,
        )

    try:
        target_contributor = Contributor.objects.get(
            id=contributor_id,
            project=project,
        )
    except Contributor.DoesNotExist:
        return Response(
            {"detail": "Contributor not found."},
            status=404,
        )

    if target_contributor.user == project.author:
        return Response(
            {"detail": "You cannot remove the author of this project."},
            status=400,
        )

    target_contributor.delete()
    return Response(status=204)
