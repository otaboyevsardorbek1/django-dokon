import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "delivery_hero.settings")
django.setup()

from restaurants.factories.restaurant import RestaurantFactory
from django.contrib.auth.models import User


def add_restaurants():
    try:
        User.objects.create_superuser(
            password='superadmin', email='admin@delivery-hero.com',
            username='Hero'
        )
    except Exception:
        pass

    RestaurantFactory.create_batch(size=20)

if __name__ == '__main__':
    add_restaurants()
