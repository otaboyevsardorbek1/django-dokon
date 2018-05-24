import graphene

from restaurants.graphql.schema import RestaurantsMutations, RestaurantsQuery


class Query(RestaurantsQuery, graphene.ObjectType):
    pass


class Mutations(RestaurantsMutations):
    pass


Schema = graphene.Schema(query=Query, mutation=Mutations)
