from django.urls import path
from .views import (
    project_collection_view,
    project_contributors_collection_view,
    project_contributor_detail_view,
)

urlpatterns = [
    path("projects/", project_collection_view, name="project-list-create"),
    path(
        "projects/<int:project_id>/contributors/",
        project_contributors_collection_view,
        name="project_contributors_collection_view",
    ),
    path(
        "projects/<int:project_id>/contributors/<int:contributor_id>/",
        project_contributor_detail_view,
        name="project_contributor_detail_view",
    ),
]
