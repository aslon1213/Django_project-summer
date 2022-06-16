from .models import Skill, Profile
from django.db.models import Q
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