from django.db import models
from django.conf import settings


class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plot(models.Model):
    SOIL_TYPES = [
        ('clay', 'Clay'),
        ('sandy', 'Sandy'),
        ('loamy', 'Loamy'),
    ]

    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='plots')
    size = models.DecimalField(max_digits=5, decimal_places=2)  # e.g. 10.50
    soil_type = models.CharField(max_length=20, choices=SOIL_TYPES)

    crop_type = models.CharField(max_length=50)
    planting_date = models.DateField()
    harvesting_date = models.DateField()

    def __str__(self):
        return f"Plot in {self.farm.name} - {self.crop_type}"
