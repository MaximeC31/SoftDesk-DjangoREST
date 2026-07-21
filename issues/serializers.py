from rest_framework.serializers import ModelSerializer
from .models import Issue
from projects.models import Contributor
from rest_framework import serializers


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "project_id",
            "author",
            "assignee",
            "priority",
            "tag",
            "status",
            "created_time",
        ]
        read_only_fields = ["id", "project_id", "author", "created_time"]

    def validate(self, attrs):
        project = self.context["project"]
        assignee = attrs.get("assignee")

        if assignee is None:
            return attrs

        is_project_contributor = Contributor.objects.filter(
            user=assignee,
            project=project,
        ).exists()

        if not is_project_contributor:
            raise serializers.ValidationError(
                "This user is not a contributor to this project."
            )

        return attrs

    def create(self, validated_data):
        project = self.context["project"]
        author = self.context["request"].user
        issue = Issue.objects.create(
            project=project,
            author=author,
            **validated_data,
        )
        return issue
