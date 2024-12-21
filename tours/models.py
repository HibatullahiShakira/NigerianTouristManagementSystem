from django.db import models

from states.models import State


class Tour(models.Model):
    TOUR_TYPES = [
        ('guided', 'Guided'),
        ('non-guided', 'Non-Guided'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    availability = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    tour_type = models.CharField(max_length=10, choices=TOUR_TYPES, default='non-guided')
    review_count = models.IntegerField(default=0, null=True, blank=True)
    state = models.ForeignKey('states.State', related_name='tours', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
