import api.views as v
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/', v.getProjects),
    path('projects/<str:pk>/', v.getProject),
    path('remove-tag/', v.delete_tag),
]