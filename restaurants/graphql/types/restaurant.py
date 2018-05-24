import graphene
from graphene_django import DjangoObjectType

from ...models import Restaurant


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant


class RestaurantInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    opens_at = graphene.Time(required=True)
    closes_at = graphene.Time(required=True)


class UpdateRestaurantInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    name = graphene.String()
    opens_at = graphene.Time()
    closes_at = graphene.Time()
