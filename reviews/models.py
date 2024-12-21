from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from NigerianTouristSystem import settings
from tours.models import Tour


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)


@receiver(post_save, sender=Review)
def update_review_count_on_save(sender, instance, created, **kwargs):
    if created:
        tour = instance.tour
        tour.review_count = tour.reviews.count()
        tour.save()


@receiver(post_delete, sender=Review)
def update_review_count_on_delete(sender, instance, **kwargs):
    tour = instance.tour
    tour.review_count = tour.reviews.count()
    tour.save()

















    def __str__(self):
        return f"Review by {self.user.username} for {self.tour.name}"














