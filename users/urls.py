from django.urls import path, reverse
from .views import *
urlpatterns = [

    path('login/', loginPage, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('registration/', registerUser, name = 'register'),

    path('', all_profiles, name = 'all_profiles'),
    path('<str:pk>/', singleprofile, name='single_profile'),
    path('account/', accountPage, name = 'account'),
    path('account_update_form/', update_profile, name = 'update_account'),
    path('delete_profile/<str:pk>',deleteProfile , name = 'delete_profile'),
    path('delete_profile_2/', delete_profile, name = 'delete_profile_2')
]