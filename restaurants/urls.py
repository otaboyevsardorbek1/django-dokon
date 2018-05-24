from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'r/(?P<restaurant_id>\d+)/?$', views.get_restaurant, name='get_restaurant'),
    url(r'r/?$', views.delete_restaurant, name='delete_restaurant')
]
