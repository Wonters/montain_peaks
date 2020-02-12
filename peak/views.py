from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializer import UserSerializer, PeakSerializer

from django.http import JsonResponse

from .models import *
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PeakViewSet(viewsets.ModelViewSet):
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer