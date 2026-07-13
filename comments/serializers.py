from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "issue",
            "author",
            "created_time",
        ]
        read_only_fields = ["id", "issue", "author", "created_time"]

    def create(self, validated_data):
        issue = self.context["issue"]
        author = self.context["request"].user
        comment = Comment.objects.create(
            issue=issue,
            author=author,
            **validated_data,
        )
        return comment
