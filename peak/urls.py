from rest_framework import serializers, routers, viewsets
from django.urls import path, include
from .views import *


# Routers for restframework BACKEND
router = routers.DefaultRouter()
router.register(r'peak', PeakViewSet, basename='peak')
router.register(r'geo', GeoViewSet, basename='geo')
router.register(r'rejected IP', IPRejViewSet)

urlpatterns = [
    # BACKEND
    path('', include(router.urls)),
    # FRONTEND
    path('view', ViewMap.as_view(), name='view map')
]