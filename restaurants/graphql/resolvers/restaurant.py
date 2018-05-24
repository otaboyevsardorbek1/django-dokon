from ...models import Restaurant


def resolve_all_restaurants(root, info):
    restaurants = Restaurant.objects.all()
    return restaurants
