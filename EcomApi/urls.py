
from django.contrib import admin
from django.urls import path, include

# Project's urlpattern
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
]