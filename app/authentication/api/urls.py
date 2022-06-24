from django.urls import path
from .views import RegisterAPIView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('users/add-user/', RegisterAPIView.as_view(), name='add-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
