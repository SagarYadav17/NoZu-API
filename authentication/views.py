# Django & Rest Framework
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

# Models
from django.contrib.auth.models import User

# Serializers
from authentication.serializers import AuthTokenPairSerializer, RegisterSerializer


class AuthTokenPairObtainView(TokenObtainPairView):
    serializer_class = AuthTokenPairSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
