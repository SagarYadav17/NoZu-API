from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rest Framework
    # Apps
    path("news/", include("news.urls")),
    path("api/blog/", include("blog.urls")),
    path("api/expense/", include("expenseTracker.urls")),
    path("api/auth/", include("authentication.urls")),
]
