from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from users_app import serializers as users_serializers
from users_app.models import Profile, Following
from django.contrib.auth.models import User

# Create your views here.


class RegistrationValidatorView(ListAPIView):
    """
    View to validate already taken emails and usernames
    """
    permission_classes = [AllowAny]
    serializer_class = users_serializers.RegistrationValidationSerializer


class RegisterView(CreateAPIView):
    """
    View for New User Registration
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = users_serializers.RegisterSerializer


class ProfileView(RetrieveUpdateDestroyAPIView):
    """
    View for User Profile to Delete and Update
    """
    permission_classes = [IsAuthenticated]
    serializer_class = users_serializers.ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user.id)
        return obj


class FollowingsView(ListAPIView):
    serializer_class = users_serializers.FollowingSerializer
    queryset = Following.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(follower=self.request.user.id)
        return obj
