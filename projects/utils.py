from .models import Project, Tag
from django.db.models import Q
def search_in_projects(request):
    search_value = ''

    if request.GET.get('search_value'):
        search_value = request.GET.get('search_value')

    tags = Tag.objects.filter(name__icontains = search_value)

    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_value) |
        Q(description__icontains = search_value) |
        Q(tags__in = tags) |
        Q(owner__name__icontains = search_value)
    )

    return projects, search_value