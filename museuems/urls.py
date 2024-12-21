from django.urls import path, include
from .views import MuseumViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('museums', MuseumViewSet, basename='museum')

urlpatterns = [
    path('', include(router.urls))
]
