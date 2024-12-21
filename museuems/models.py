from django.db import models
from django.apps import apps
from states.models import State


class Museum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='museums')

    def __str__(self):
        return self.name
