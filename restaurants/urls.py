from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'restaurant/(?P<restaurant_id>\d+)/?$', views.get_restaurant, name='get_restaurant'),
    url(r'restaurant/?$', views.delete_restaurant, name='delete_restaurant')
]
