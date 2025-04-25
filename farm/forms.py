from django import forms
from .models import Farm, Plot


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'location', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-input'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Location',
                'class': 'form-input'
            }),
            'latitude': forms.NumberInput(attrs={
                'placeholder': 'Latitude',
                'class': 'form-input'
            }),
            'longitude': forms.NumberInput(attrs={
                'placeholder': 'Longitude',
                'class': 'form-input'
            }),
        }

class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ['farm', 'size', 'soil_type', 'crop_type', 'planting_date', 'harvesting_date']
        widgets = {
            'farm': forms.Select(attrs={
                'class': 'form-input'
            }),
            'size': forms.NumberInput(attrs={
                'placeholder': 'Plot Size (e.g. 2.5)',
                'class': 'form-input'
            }),
            'soil_type': forms.TextInput(attrs={
                'placeholder': 'Soil Type',
                'class': 'form-input'
            }),
            'crop_type': forms.TextInput(attrs={
                'placeholder': 'Crop Type',
                'class': 'form-input'
            }),
            'planting_date': forms.DateInput(attrs={
                'placeholder': 'Planting Date',
                'type': 'date',
                'class': 'form-input'
            }),
            'harvesting_date': forms.DateInput(attrs={
                'placeholder': 'Harvesting Date',
                'type': 'date',
                'class': 'form-input'
            }),
        }
