from django.urls import path
from . import views

urlpatterns = [
    # path('', gps_data, name='gps_data')
    path('', views.GPSDataListCreate.as_view(), name='gps_data'),
    path('location/', views.show_last_location, name='last_location'),
]
