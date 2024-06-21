from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Includes URLs from the blog app
    path('members/', include('django.contrib.auth.urls')),  # Includes default authentication URLs
    path('members/', include('members.urls')),  # Includes URLs from the members app
    # Add other URL patterns here as needed
]
