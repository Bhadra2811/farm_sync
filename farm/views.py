from django.shortcuts import render, redirect, get_object_or_404
from .models import Farm, Plot
from .forms import FarmForm, PlotForm
from django.contrib.auth.decorators import login_required

@login_required
def farm_list(request):
    query = request.GET.get('q')
    farms = Farm.objects.filter(owner=request.user)
    
    if query:
        farms = farms.filter(
            models.Q(name__icontains=query) | models.Q(location__icontains=query)
        )

    return render(request, 'farm/farm_list.html', {'farms': farms, 'query': query})

@login_required
def farm_add(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.owner = request.user
            farm.save()
            return redirect('farm-list')
    else:
        form = FarmForm()
    return render(request, 'farm/farm_form.html', {'form': form})

@login_required
def farm_edit(request, pk):
    farm = get_object_or_404(Farm, pk=pk, owner=request.user)
    form = FarmForm(request.POST or None, instance=farm)
    if form.is_valid():
        form.save()
        return redirect('farm-list')
    return render(request, 'farm/farm_form.html', {'form': form})

@login_required
def farm_delete(request, pk):
    farm = get_object_or_404(Farm, pk=pk, owner=request.user)
    farm.delete()
    return redirect('farm-list')

@login_required
def plot_list(request):
    plots = Plot.objects.filter(farm__owner=request.user)
    return render(request, 'farm/plot_list.html', {'plots': plots})

@login_required
def plot_add(request):
    if request.method == 'POST':
        form = PlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plot-list')
    else:
        form = PlotForm()
    return render(request, 'farm/plot_form.html', {'form': form})

@login_required
def plot_edit(request, pk):
    plot = get_object_or_404(Plot, pk=pk, farm__owner=request.user)
    form = PlotForm(request.POST or None, instance=plot)
    if form.is_valid():
        form.save()
        return redirect('plot-list')
    return render(request, 'farm/plot_form.html', {'form': form})

@login_required
def plot_delete(request, pk):
    plot = get_object_or_404(Plot, pk=pk, farm__owner=request.user)
    plot.delete()
    return redirect('plot-list')

@login_required
def farm_map(request, pk):
    farm = get_object_or_404(Farm, pk=pk, owner=request.user)
    return render(request, 'farm/farm_map.html', {'farm': farm})
