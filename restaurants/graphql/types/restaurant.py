from graphene_django import DjangoObjectType
import graphene

from ...models import Restaurant


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant


class RestaurantInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    opens_at = graphene.Time(required=True)
    closes_at = graphene.Time(required=True)
