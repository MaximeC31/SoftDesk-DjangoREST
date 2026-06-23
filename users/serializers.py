from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    age = serializers.IntegerField()
    can_be_contacted = serializers.BooleanField(required=True)
    can_data_be_shared = serializers.BooleanField(required=True)

    def validate(self, attrs):
        if "username" not in attrs:
            raise ValidationError("Username is required.")
        if "password" not in attrs:
            raise ValidationError("Password is required.")
        if "age" not in attrs:
            raise ValidationError("Age is required.")
        if "can_be_contacted" not in attrs:
            raise ValidationError("Consent to be contacted is required.")
        if "can_data_be_shared" not in attrs:
            raise ValidationError("Consent to share data is required.")

        age_input = self.initial_data["age"]

        if type(age_input) is not int:
            raise ValidationError({"age": "Age must be an integer."})

        if age_input < 15:
            raise ValidationError("Age must be 15 or older.")

        return attrs

    def create(self, validated_data):
        User = get_user_model()
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
