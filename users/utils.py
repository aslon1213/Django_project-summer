from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginate_profiles(request, profiles, objects_num):

    page = request.GET.get('page')
    page_profiles_number = objects_num

    paginator = Paginator(profiles, page_profiles_number)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages()
        profiles = paginator.page(page)
    

    left = int(page) - 2
    if left < 1:
        left = 1
    right = int(page) + 3
    if right > paginator.num_pages:
        right = paginator.num_pages + 1

    custom_range = range(left,right)

    return profiles, custom_range


def search_in_profiles(request):
    search_value = ''

    if request.GET.get('search_value'):
        search_value = request.GET.get('search_value')

    skills = Skill.objects.filter(name__icontains = search_value)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = search_value) |
        Q(bio__icontains = search_value) |
        Q(skill__in = skills)
    )
    return profiles, search_value