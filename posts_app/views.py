from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from posts_app.serializers import PostSerializer, UpdatePostSerializer
from posts_app.models import Post
from django.db.utils import IntegrityError

# Create your views here.


class CreatePostView(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = self.request.user
        title = data['title']
        description = data['description']

        try:
            post = Post.objects.create(
                user=user, title=title, description=description)

            post.save()

            return Response({'status': 'success'}, status=HTTP_201_CREATED)
        except IntegrityError:
            return Response({'status': 'title & description fields are required'}, HTTP_400_BAD_REQUEST)


class UpdatePostView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdatePostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class NewsFeed(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title']
    ordering_fields = ['timestamp', 'user']
    ordering = ['-timestamp']
