from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('',projects, name = 'projects'),
    path('project/<str:pk>/', project, name="project"),

]