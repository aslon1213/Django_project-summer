from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_projects(request, projects, objects_num):

    page = request.GET.get('page')
    page_projects_number = objects_num

    paginator = Paginator(projects, page_projects_number)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages()
        projects = paginator.page(page)
    

    left = int(page) - 3
    if left < 1:
        left = 1
    right = int(page) + 4
    if right > paginator.num_pages:
        right = paginator.num_pages + 1

    custom_range = range(left,right)

    return projects, custom_range


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