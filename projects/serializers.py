from django.contrib.auth import get_user_model
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
    contributor_id = serializers.IntegerField(source="id", read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source="user",
        queryset=get_user_model().objects.all(),
    )
    project_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Contributor
        fields = ["contributor_id", "user_id", "project_id", "created_time"]
        read_only_fields = ["contributor_id", "project_id", "created_time"]

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
