from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This username is already taken.",
            ),
        ],
    )
    password = serializers.CharField(write_only=True)
    can_be_contacted = serializers.BooleanField(required=True)
    can_data_be_shared = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "age",
            "can_be_contacted",
            "can_data_be_shared",
        ]
        read_only_fields = ["id"]

    def validate_password(self, password):
        validate_password(password)
        return password

    def validate(self, attrs):
        if type(self.initial_data.get("age")) is not int:
            raise serializers.ValidationError(
                {
                    "age": "Age must be an integer.",
                }
            )
        if type(self.initial_data.get("can_be_contacted")) is not bool:
            raise serializers.ValidationError(
                {
                    "can_be_contacted": (
                        "Consent to be contacted must be a boolean value."
                    ),
                }
            )
        if type(self.initial_data.get("can_data_be_shared")) is not bool:
            raise serializers.ValidationError(
                {
                    "can_data_be_shared": (
                        "Consent to share data must be a boolean value."
                    ),
                }
            )

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
