from rest_framework import permissions, views, generics, filters
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from posts_app.serializers import PostSerializer
from posts_app.models import Post

# Create your views here.


class PostsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class UpdatePostView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class NewsFeed(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title']
    ordering_fields = ['timestamp', 'user']
    ordering = ['-timestamp']
