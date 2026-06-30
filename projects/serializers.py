from rest_framework import serializers
from .models import Contributor, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author",
            "created_time",
        ]
        read_only_fields = ["id", "author", "created_time"]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "created_time"]
        read_only_fields = ["id", "project", "created_time"]

    def validate(self, attrs):
        user = attrs["user"]
        project = self.context["project"]
        if Contributor.objects.filter(user=user, project=project).exists():
            raise serializers.ValidationError(
                "This user is already a contributor to this project."
            )
        return attrs

    def create(self, validated_data):
        project = self.context["project"]
        return Contributor.objects.create(project=project, **validated_data)
