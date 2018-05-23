import faker
from factory import DjangoModelFactory, SubFactory, Sequence
import random
from faker.providers import BaseProvider
from ..models import Restaurant

fake = faker.Factory.create()


class TimeProvider(BaseProvider):
    def time_generator(self, prev_hh: int=None):
        if prev_hh:
            hh = random.randint(prev_hh + 1, 23)
        else:
            hh = random.randint(1, 12)
        mm = random.randint(0, 59)

        # We select a random destination from the list and return it
        return f"{hh}:{mm}"


fake.add_provider(TimeProvider)


class RestaurantFactory(DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = Sequence(lambda n: fake.sentence(nb_words=4))
    opens_at = Sequence(lambda n: fake.time_generator())
