from django.urls import path
from .views import project_collection_view

urlpatterns = [
    path("projects/", project_collection_view, name="project-list-create"),
]
