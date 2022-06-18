from django.urls import path
from . import views

urlpatterns = [
    #authoriztion and registration
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    #account
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="single_profile"),
    path('account/', views.userAccount, name="account"),

    path('edit-account/', views.editAccount, name="update_account"),
    #skill CRUD
    path('create_skill/', views.createSkill, name = 'create_skill'),
    path('update_skill/<str:pk>', views.updateSkill, name = 'update_skill'),
    path('delete_skill/<str:pk>', views.deleteSkill, name = 'delete_skill'),
    #messages
    path('inbox/', views.inbox, name = 'inbox'),
    path('message/<str:pk>/', views.single_message, name = 'message'),
    path('send_message/<str:pk>/', views.create_message, name = 'send_message'),
]
