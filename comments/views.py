from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from issues.models import Issue
from projects.models import Contributor, Project

from .models import Comment
from .serializers import CommentSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def project_issue_comments_collection_view(request, project_id, issue_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=404)

    is_contributor = Contributor.objects.filter(
        user=request.user,
        project=project,
    ).exists()

    if not is_contributor:
        return Response(
            {"detail": "You are not a contributor to this project."},
            status=403,
        )

    try:
        issue = Issue.objects.get(id=issue_id, project=project)
    except Issue.DoesNotExist:
        return Response({"detail": "Issue not found."}, status=404)

    comments = Comment.objects.filter(issue=issue)

    match request.method:
        case "GET":
            comments = (
                comments.select_related("issue", "issue__project", "author")
                .order_by("-created_time")
            )
            paginator = PageNumberPagination()
            paginator.page_size = 10
            paginated_comments = paginator.paginate_queryset(comments, request)
            serializer = CommentSerializer(paginated_comments, many=True)
            return paginator.get_paginated_response(serializer.data)

        case "POST":
            serializer = CommentSerializer(
                data=request.data,
                context={"issue": issue, "request": request},
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

        case _:
            return Response(status=405)


@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def project_issue_comment_detail_view(
    request,
    project_id,
    issue_id,
    comment_id,
):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=404)

    is_contributor = Contributor.objects.filter(
        user=request.user,
        project=project,
    ).exists()

    if not is_contributor:
        return Response(
            {"detail": "You are not a contributor to this project."},
            status=403,
        )

    try:
        issue = Issue.objects.get(id=issue_id, project=project)
    except Issue.DoesNotExist:
        return Response({"detail": "Issue not found."}, status=404)

    try:
        comment = Comment.objects.get(id=comment_id, issue=issue)
    except Comment.DoesNotExist:
        return Response({"detail": "Comment not found."}, status=404)

    match request.method:
        case "GET":
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=200)

        case "PATCH":
            if request.user != comment.author:
                return Response(
                    {"detail": "You are not the author of this comment."},
                    status=403,
                )

            serializer = CommentSerializer(
                instance=comment,
                data=request.data,
                partial=True,
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)

        case "DELETE":
            if request.user != comment.author:
                return Response(
                    {"detail": "You are not the author of this comment."},
                    status=403,
                )
            comment.delete()
            return Response(status=204)
        case _:
            return Response(status=405)
