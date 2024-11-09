from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GPSData
from .serializers import GPSDataSerializer



class GPSDataListCreate(generics.ListCreateAPIView):
    queryset = GPSData.objects.all()
    serializer_class = GPSDataSerializer

    def get_queryset(self):
        return GPSData.objects.all().order_by('-id')[:20]


# @api_view(['POST'])
# def gps_data(request):
#     if request.method == 'POST':
#         serializer = GPSDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
