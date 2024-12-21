from django.db import models


class Tribe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    state = models.ManyToManyField('states.State', related_name='tribe_states')
    festivals = models.CharField(max_length=150, null=False, blank=False)
