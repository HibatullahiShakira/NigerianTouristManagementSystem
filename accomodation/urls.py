from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccommodationViewSet

router = DefaultRouter()
router.register('accommodations', AccommodationViewSet, basename='accommodations')

urlpatterns = [
    path('', include(router.urls)),
]
