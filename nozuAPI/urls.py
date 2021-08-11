from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path(
        'api-auth/',
        include('rest_framework.urls'),
    ),

    # Password Reset Package
    path(
        'password_reset/',
        include('django_rest_passwordreset.urls'),
    ),

    # Apps
    path('', include('users_app.urls')),
    path('', include('posts_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
