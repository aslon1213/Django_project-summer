from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('',projects, name = 'projects'),
    path('project/<str:pk>/', project, name="project"),
    path('create-project/',new_project, name = "create_project"),
    path('update-project/<str:pk>/', updateProject, name = 'update-project'),
    path('delete-project/<str:pk>/', deleteProject, name = 'delete-project'),
]