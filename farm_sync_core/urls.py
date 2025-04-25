from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('farms/', include('farm.urls')),
    path('', include('users.urls')),
]