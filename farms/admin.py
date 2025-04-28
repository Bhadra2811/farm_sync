from django.contrib import admin
from .models import Farm, Plot, Crop

admin.site.register(Farm)
admin.site.register(Plot)
admin.site.register(Crop)