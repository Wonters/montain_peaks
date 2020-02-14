from rest_framework import serializers, routers, viewsets
from django.urls import path, include
from .views import *


# Routers for restframework BACKEND
router = routers.DefaultRouter()
router.register(r'peak', PeakViewSet)
router.register(r'geo', GeoPeakList, basename='geo bb')

urlpatterns = [
    # BACKEND
    path('', include(router.urls)),
    # FRONTEND
    path('view', ViewMap.as_view(), name='view map')
]