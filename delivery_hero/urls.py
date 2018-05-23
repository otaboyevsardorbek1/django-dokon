from django.contrib import admin
from django.urls import path, include
from django.conf.urls import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/admin', permanent=True)),
    re_path(r'^', include('restaurants.urls')),
    path('admin/', admin.site.urls),
]
