from django.urls import path
from blog.views import *

urlpatterns = [
    path("posts/", BlogPostListView.as_view(), name="blog-posts"),
    path("posts/<slug:slug>/", BlogPostDetailView.as_view(), name="blog-post-detail"),
]
