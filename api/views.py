
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projects.models import Project, Tag
from .serializers import ProjectsSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectsSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProject(request, pk):
    project = Project.objects.get(id = pk)
    serializer = ProjectsSerializer(project, many = False)
    return Response(serializer.data)

@permission_classes([IsAuthenticated])
def getTags(request):
    pass

@api_view(["DELETE"])
def delete_tag(request):
    tag_id = request.data['tag']
    project_id = request.data['project']


    project = Project.objects.get(id = project_id)
    tag = Tag.objects.get(id = tag_id)

    project.tags.remove(tag)

    return Response("Tag was deleted!")

#get_____