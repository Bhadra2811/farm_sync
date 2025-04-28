from django.db import models
from accounts.models import CustomUser

class Farm(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='farms')
    created_at = models.DateTimeField(auto_now_add=True)  # This field might be the culprit

    def __str__(self):
        return self.name
class Plot(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='plots')
    size = models.FloatField()
    soil_type = models.CharField(max_length=50, choices=[('loamy', 'Loamy'), ('sandy', 'Sandy'), ('clay', 'Clay')])
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  # Check here

class Crop(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='crops')
    crop_type = models.CharField(max_length=50, choices=[('wheat', 'Wheat'), ('rice', 'Rice'), ('corn', 'Corn')])
    planting_date = models.DateField()
    harvesting_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)  # Check here