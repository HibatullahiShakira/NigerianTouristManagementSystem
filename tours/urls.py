from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework.routers import DefaultRouter

from reviews.views import ReviewViewSet
from tours.views import TourViewSet

router = DefaultRouter()

router.register('tours', TourViewSet, basename='tours')

tours_router = NestedDefaultRouter(router, 'tours', lookup='tour')
#tours_router.register('users', UserViewSet, basename='users')
tours_router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.urls + tours_router.urls
