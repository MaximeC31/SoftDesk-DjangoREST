from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, ProfileSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    user = serializer.save()
    return Response(ProfileSerializer(user).data, status=201)


@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user

    match request.method:
        case "GET":
            serializer = ProfileSerializer(user)
            return Response(serializer.data, status=200)

        case "PATCH":
            serializer = ProfileSerializer(
                user,
                data=request.data,
                partial=True,
            )
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            serializer.save()
            return Response(serializer.data, status=200)

        case "DELETE":
            user.delete()
            return Response(status=204)

        case _:
            return Response({"detail": "Method not allowed."}, status=405)
