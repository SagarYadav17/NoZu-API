from django.urls import path
from posts_app import views

urlpatterns = [
    path('posts/create/', views.CreatePostView.as_view(), name='create-post'),
    path('profile/posts/<int:id>/', views.UpdatePostView.as_view(), name='post'),
    path('feed/', views.NewsFeed.as_view(), name='feed'),
]
