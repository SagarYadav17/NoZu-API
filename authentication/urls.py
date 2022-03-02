from django.urls import path
from authentication import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", views.RegisterUserView.as_view(), name="auth_register"),
    path("login/", views.AuthTokenPairObtainView.as_view(), name="auth_token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="auth_token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="auth_logout"),
]
