from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Peak



class PeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ['id', 'name', 'lon', 'lat', 'altitude']

class GeoBBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ['name', 'get_geo_bb']




