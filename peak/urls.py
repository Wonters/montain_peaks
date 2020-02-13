from rest_framework import serializers, routers, viewsets
from django.urls import path
from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'peak', PeakViewSet)

urlpatterns = [

]
urlpatterns += router.urls
