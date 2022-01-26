from rest_framework.generics import ListAPIView, RetrieveAPIView
from datetime import date

# Models
from blog.models import Post

# Serializers
from blog.serializers import PostDetailSerializer, PostListSerializer


class BlogPostListView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(is_active=True, published_date__lte=date.today()).order_by("-published_date")

        q = self.request.query_params.get("q")
        if q:
            queryset = queryset.filter(title__icontains=q)

        return queryset


class BlogPostDetailView(RetrieveAPIView):
    queryset = Post.objects.filter(is_active=True, published_date__lte=date.today()).order_by("-published_date")
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
