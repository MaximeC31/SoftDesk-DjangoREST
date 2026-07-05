from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projects.models import Project, Contributor
from .models import Issue
from .serializers import IssueSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def project_issues_collection_view(request, project_id):
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
            issues = (
                Issue.objects.filter(
                    project=project,
                )
                .select_related(
                    "project",
                    "author",
                    "assignee",
                )
                .order_by("-created_time")
            )

            paginator = PageNumberPagination()
            paginator.page_size = 10
            paginated_issues = paginator.paginate_queryset(issues, request)

            serializer = IssueSerializer(paginated_issues, many=True)
            return paginator.get_paginated_response(serializer.data)

        case "POST":
            serializer = IssueSerializer(
                data=request.data,
                context={"project": project, "request": request},
            )

            if not serializer.is_valid():
                return Response(serializer.errors, status=400)

            issue = serializer.save()
            return Response(
                IssueSerializer(issue).data,
                status=201,
            )
