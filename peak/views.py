from rest_framework import viewsets
from .serializer import PeakSerializer, GeoBBSerializer
from rest_framework import mixins
from django.views.generic import TemplateView
from django.http import request
from .models import Peak
import json


'''
BACKEND
'''
class PeakViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `create`,`read`,`update` and `delete` peak.
    """
    queryset = Peak.objects.all().order_by('-altitude')
    serializer_class = PeakSerializer


class GeoPeakList(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `list` peak in geographical bounding box.
    """
    queryset = Peak.objects.all().order_by('-altitude')
    serializer_class = GeoBBSerializer


'''
FRONTEND
'''

class ViewMap(TemplateView):
    template_name = 'peak/map.html'
