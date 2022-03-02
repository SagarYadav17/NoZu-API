# Django & Rest Framework
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Models
from django.contrib.auth.models import User
from rest_framework_simplejwt.models import TokenUser

# Serializers
from authentication.serializers import AuthTokenPairSerializer, RegisterSerializer


class AuthTokenPairObtainView(TokenObtainPairView):
    serializer_class = AuthTokenPairSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # request.user.auth_token.delete()
        print(request.user)
        return Response()
