from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    user = serializer.save()

    safe_user_data = {
        "id": user.id,
        "username": user.username,
        "age": user.age,
        "can_be_contacted": user.can_be_contacted,
        "can_data_be_shared": user.can_data_be_shared,
    }

    return Response(safe_user_data, status=201)
