from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, PeakSerializer
from rest_framework.views import APIView
from django.http import Http404

from .models import Peak, User
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PeakViewSet(viewsets.ModelViewSet):
    queryset = Peak.objects.all().order_by('-altitude')
    serializer_class = PeakSerializer


class PeakList(APIView):
    def get(self, request, format = None):
        peaks = Peak.objects.all()
        serializer = PeakSerializer(peaks, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = PeakSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeakDetail(APIView):

    def get_object(self,pk):
        try:
            return Peak.objects.get(pk=pk)
        except Peak.DoesNotExist:
            raise Http404

    def get(self,request,pk, fromat=None):
        peak = self.get_object(pk)
        serializer = PeakSerializer(peak)
        return  Response(serializer.data)


    def put(self, request, pk , format = None):
        peak = self.get_object(pk)
        serializer = PeakSerializer(peak, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        peak = self.get_object(pk)
        peak.delete()



