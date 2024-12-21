from django.db import models

from tribes.models import Tribe


class Cuisine(models.Model):
    FOOD_CLASS = [
        ('traditional', 'TRADITIONAL'),
        ('salad', 'SALAD'),
        ('street_food', 'STREET-FOOD'),
        ('soup', 'SOUP'),
        ('desserts', 'DESSERTS'),
        ('main_course', 'MAIN_COURSE'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    food_health = models.CharField(max_length=100, choices=FOOD_CLASS)
    food_class = models.CharField(max_length=100)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE, related_name='tribe_states')
