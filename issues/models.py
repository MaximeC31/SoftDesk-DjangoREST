from django.db import models
from django.conf import settings


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authored_issues",
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_issues",
    )
    priority = models.CharField(
        max_length=20,
        choices=[
            ("LOW", "Low"),
            ("MEDIUM", "Medium"),
            ("HIGH", "High"),
        ],
    )
    tag = models.CharField(
        max_length=20,
        choices=[
            ("BUG", "Bug"),
            ("FEATURE", "Feature"),
            ("TASK", "Task"),
        ],
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("To Do", "To Do"),
            ("In Progress", "In Progress"),
            ("Finished", "Finished"),
        ],
        default="To Do",
    )
    created_time = models.DateTimeField(auto_now_add=True)
