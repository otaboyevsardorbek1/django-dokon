from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/admin', permanent=True)),
    url(r'^', include('restaurants.urls')),
    url(r'^graphql/?', include('api.urls')),
    url('admin/', admin.site.urls),
]
