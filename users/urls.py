from django.urls import path, reverse
from .views import *
urlpatterns = [

    path('login/', loginUser, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('registration/', registerUser, name = 'register'),

    path('', profiles, name = 'profiles'),
    path('<str:pk>/', userProfile, name='single_profile'),
    path('account/', userAccount, name = 'account'),
    path('account_update_form/', editAccount, name = 'update_account'),
]
