from rest_framework import viewsets
from rest_framework.exceptions import APIException
from .serializer import PeakSerializer, GeoBBSerializer, IPRejSerializer
from rest_framework import mixins, response, status
from django.views.generic import TemplateView
from .models import Peak, IPRejected
from rest_framework import permissions
import json
from urllib.request import urlopen

'''
PERMISSIONS
'''
whiteList = (
    'UK',
    'FR',
    'US',
    'Germany',
)


class IPPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            client_adress = request.META['HTTP_X_FORWARDED_FOR']
        except:
            client_adress = request.META['REMOTE_ADDR']

        if client_adress == '':
            url = 'https://ipinfo.io/json'
        else:
            url = 'https://ipinfo.io/' + client_adress + '/json'
        res = urlopen(url)
        data = json.load(res)
        try :
            if 'bogon' in data.keys():
                if data['bogon'] == True:
                    ret = True
                    print('IP is local')
            elif 'country' in data.keys():
                if data['country'] in whiteList:
                    ret = True
                    print('IP is whitelisted')
        except:
            self.message = "This IP is not whitelisted [{}]".format(data['ip'])
            if not IPRejected.objects.filter(ip=data['ip']).exists():
                mod = IPRejected.objects.create(ip=data['ip'])
                mod.save()
            ret = False
        return ret

'''
BACKEND
'''
class PeakViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `create`,`read`,`update` and `delete` peak.
    """
    queryset = Peak.objects.all().order_by('-altitude')
    serializer_class = PeakSerializer
    permission_classes = [permissions.AllowAny,IPPermission]



class GeoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `list` peak in geographical bounding box.
    """
    queryset = Peak.objects.all().order_by('-altitude')
    serializer_class = GeoBBSerializer
    permission_classes = [permissions.AllowAny,IPPermission]

class IPRejViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides `list` rejected IP adresses.
    """
    queryset = IPRejected.objects.all().order_by('-id')
    serializer_class = IPRejSerializer
    permission_classes = [permissions.IsAuthenticated]

'''
FRONTEND
'''
class ViewMap(TemplateView):
    template_name = 'peak/map.html'
