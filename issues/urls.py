from django.urls import path
from .views import project_issues_collection_view

urlpatterns = [
    path(
        "projects/<int:project_id>/issues/",
        project_issues_collection_view,
        name="project_issues_collection_view",
    ),
]
