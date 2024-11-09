from django.db import models

class GPSData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lat: {self.latitude}, Lon: {self.longitude}"
