from django.urls import path
from django.conf.urls import re_path

from . import views

urlpatterns = [
    re_path(r'r/(?P<restaurant_id>\d+)/?$', views.get_restaurant, name='get_restaurant'),
    re_path(r'r/?$', views.delete_restaurant, name='delete_restaurant')
]
