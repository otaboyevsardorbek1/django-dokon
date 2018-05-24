import faker
from factory import DjangoModelFactory, Sequence, LazyAttribute
import random
from faker.providers import BaseProvider
from ..models import Restaurant

fake = faker.Factory.create()


class TimeProvider(BaseProvider):
    def time_generator(self, prev_hh: str=None):
        if prev_hh:
            val_hh = prev_hh.split(':')[0]
            hh = random.randint(int(val_hh) + 1, 23)
        else:
            hh = random.randint(1, 12)
        if hh < 10:
            hh = f'0{hh}'
        mm = random.randint(0, 59)
        if mm < 10:
            mm = f'0{mm}'

        # We select a random destination from the list and return it
        return f"{hh}:{mm}"


fake.add_provider(TimeProvider)


class RestaurantFactory(DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = Sequence(lambda n: fake.company()[:99])
    opens_at = Sequence(lambda n: fake.time_generator())
    closes_at = LazyAttribute(lambda o: fake.time_generator(o.opens_at))

