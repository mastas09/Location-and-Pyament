from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gps_data/', include('gps_data.urls')),
    path('payment/', include('payment.urls')),
]
