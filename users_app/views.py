from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE
from users_app import serializers as users_serializers
from users_app.models import Profile, Following
from django.contrib.auth.models import User

# Create your views here.


class RegistrationValidatorView(ListAPIView):
    """
    View to validate already taken emails and usernames
    """
    permission_classes = (AllowAny,)
    serializer_class = users_serializers.RegistrationValidationSerializer
    queryset = User.objects.all()


class RegisterView(CreateAPIView):
    """
    View for New User Registration
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = users_serializers.RegisterSerializer


class ProfileView(RetrieveAPIView):
    """
    View for User Profile to Delete and Update
    """
    # permission_classes = (IsAuthenticated,)
    serializer_class = users_serializers.ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        username = self.kwargs['username']
        queryset = self.filter_queryset(self.get_queryset())
        user_obj = get_object_or_404(User, username=username)
        obj = queryset.get(user=user_obj)

        return obj

    def post(self, request, username):
        if username == self.request.user.username:
            return Response(status=HTTP_200_OK)

        else:
            return Response({"error": "You don't have permission to perform that activity"}, status=HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, username):
        if username == self.request.user.username:
            Profile.objects.filter(user__username=username).delete()
            return Response({"status": "User Profile is deleted"}, status=HTTP_200_OK)

        else:
            return Response({"error": "You don't have permission to perform that activity"}, status=HTTP_406_NOT_ACCEPTABLE)


class FollowingsView(ListAPIView):
    """
    List of profiles you follow
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = users_serializers.FollowingSerializer
    queryset = Following.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(follower=self.request.user.id)
        return obj
