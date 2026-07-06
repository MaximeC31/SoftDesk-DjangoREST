from django.urls import path
from .views import project_issues_collection_view, project_issue_detail_view

urlpatterns = [
    path(
        "projects/<int:project_id>/issues/",
        project_issues_collection_view,
        name="project_issues_collection_view",
    ),
    path(
        "projects/<int:project_id>/issues/<int:issue_id>/",
        project_issue_detail_view,
        name="project_issue_detail_view",
    ),
]
