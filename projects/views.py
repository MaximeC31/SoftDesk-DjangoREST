from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Contributor
from .serializers import ProjectSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def project_collection_view(request):
    serializer = ProjectSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    project_instance = serializer.save(author=request.user)
    Contributor.objects.create(user=request.user, project=project_instance)

    return Response(ProjectSerializer(project_instance).data, status=201)
