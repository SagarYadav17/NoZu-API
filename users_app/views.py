from django.shortcuts import render
from rest_framework import generics, permissions
from users_app import serializers
from users_app.models import Profile
from django.contrib.auth.models import User

# Create your views here.


class RegisterView(generics.CreateAPIView):
    """
    View for New User Registration
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegisterSerializer


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for User Profile to Delete and Update
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user.id)
        return obj
