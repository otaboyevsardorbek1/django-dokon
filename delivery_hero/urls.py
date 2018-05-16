from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('restaurants/', include('restaurants.urls')),
    path('admin/', admin.site.urls),
]
