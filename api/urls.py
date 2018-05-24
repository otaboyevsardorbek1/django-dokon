from django.conf.urls import url

from .views import HeroGraphQLView

urlpatterns = [
    url(r'^$', HeroGraphQLView, name='graphql'),
]
