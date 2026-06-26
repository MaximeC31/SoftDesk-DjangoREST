from django.contrib import admin
from .models import Contributor, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "type", "author", "created_time"]
    list_filter = ["type", "created_time"]
    search_fields = ["title", "description", "author__username"]


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "project", "created_time"]
    search_fields = ["user__username", "project__title"]
