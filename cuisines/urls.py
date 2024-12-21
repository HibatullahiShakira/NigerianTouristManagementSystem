from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuisineViewSet

router = DefaultRouter()
router.register('cuisines', CuisineViewSet, basename='cuisines')

urlpatterns = [
    path('', include(router.urls)),
]
