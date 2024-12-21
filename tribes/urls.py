from  django.urls import path, include
from .views import TribeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('tribes', TribeViewSet, basename='tribes')

urlpatterns = [
    path('', include(router.urls))
]