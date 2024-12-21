from django.db import models

from cuisines.models import Cuisine
from museuems.models import Museum
from tribes.models import Tribe


class State(models.Model):
    GEOPOLITICAL_ZONES = [
        ('North Central', 'North Central'),
        ('North East', 'North East'),
        ('North West', 'North West'),
        ('South East', 'South East'),
        ('South South', 'South South'),
        ('South West', 'South West'),

    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    tribes = models.ManyToManyField(Tribe, related_name='+')
    museums = models.ManyToManyField(Museum, related_name='+')
    geopolitical_zones = models.CharField(max_length=15, choices=GEOPOLITICAL_ZONES)

    def __str__(self):
        return self.name + '\n' + self.geopolitical_zones
