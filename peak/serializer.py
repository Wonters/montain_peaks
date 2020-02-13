from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Peak




# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ['id', 'name', 'get_geo_bb', 'altitude']




