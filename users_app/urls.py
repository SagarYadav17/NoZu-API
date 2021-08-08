from django.urls import path
from users_app import views as users_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('registered-users/', users_view.RegistrationValidatorView.as_view(),
         name='registered-users'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', users_view.RegisterView.as_view(), name='register'),
    path('profile/', users_view.ProfileView.as_view(), name='profile'),
    path('profile/followings/', users_view.FollowingsView.as_view(), name='followings'),
]
