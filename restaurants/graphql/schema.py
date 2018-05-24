import graphene

from .mutations import *
from .resolvers import *
from .types import *


class RestaurantsMutations(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
    update_restaurant = UpdateRestaurant.Field()


class RestaurantsQuery(graphene.ObjectType):
    get_all_restaurants = graphene.List(
        RestaurantType, resolver=resolve_all_restaurants
    )
