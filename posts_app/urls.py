from django.urls import path
from posts_app import views

urlpatterns = [
    path('profile/posts/', views.PostsView.as_view(), name='user-posts'),
    path('profile/posts/<int:id>/', views.UpdatePostView.as_view(), name='post'),
    path('feed/', views.NewsFeed.as_view(), name='feed'),
]
