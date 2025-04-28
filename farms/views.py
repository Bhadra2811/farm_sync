from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Farm, Plot, Crop
from accounts.models import CustomUser

@login_required
def farm_list(request):
    farms = Farm.objects.filter(owner=request.user)
    return render(request, 'farms/farm_list.html', {'farms': farms})

@login_required
def farm_detail(request, farm_id):
    # Get the farm by ID, ensuring it belongs to the logged-in user
    farm = get_object_or_404(Farm, id=farm_id, owner=request.user)
    plots = farm.plots.all()  # Get all plots for this farm
    return render(request, 'farms/farm_detail.html', {
        'farm': farm,
        'plots': plots,
    })
    
@login_required
def dashboard(request):
    if request.user.role != 'manager':
        return redirect('farm_list')
    total_farms = Farm.objects.count()
    total_plots = Plot.objects.count()
    total_crops = Crop.objects.count()
    farms = Farm.objects.all()
    return render(request, 'farms/dashboard.html', {
        'total_farms': total_farms,
        'total_plots': total_plots,
        'total_crops': total_crops,
        'farms': farms,
    })