
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('Students.urls')),
    path('library/', include('Library.urls')),
    path('auth/', include('Authentication.urls')),
]
