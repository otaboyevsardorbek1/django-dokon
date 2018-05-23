from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    opens_at = models.TimeField(blank=False, null=False)
    closes_at = models.TimeField(blank=False, null=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (
            f'{type(self).__name__}'
            f'(id="{self.id}", name="{self.name}")'
        )
