from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GPSData
from .serializers import GPSDataSerializer


class GPSDataListCreate(generics.ListCreateAPIView):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

    def get_queryset(self):
        return GPSData.objects.all().order_by('-id')[:20]
    

def show_last_location(request):
    # Get the latest GPSData entry
    last_location = GPSData.objects.latest('timestamp')
    context = {
        'latitude': last_location.latitude,
        'longitude': last_location.longitude,
    }
    return render(request, 'last_location.html', context)
