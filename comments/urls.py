from django.urls import path

from .views import (
    project_issue_comment_detail_view,
    project_issue_comments_collection_view,
)

urlpatterns = [
    path(
        "projects/<int:project_id>/issues/<int:issue_id>/comments/",
        project_issue_comments_collection_view,
        name="project_issue_comments_collection_view",
    ),
    path(
        "projects/<int:project_id>/issues/<int:issue_id>/comments/"
        "<uuid:comment_id>/",
        project_issue_comment_detail_view,
        name="project_issue_comment_detail_view",
    ),
]
