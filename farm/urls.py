from django.urls import path
from .views import (
    farm_list, farm_add, farm_edit, farm_delete,
    plot_list, plot_add, plot_edit, plot_delete, farm_map
)



urlpatterns = [
    path('', farm_list, name='farm-list'),
    path('add/', farm_add, name='farm-add'),
    path('edit/<int:pk>/', farm_edit, name='farm-edit'),
    path('delete/<int:pk>/', farm_delete, name='farm-delete'),
    path('plots/', plot_list, name='plot-list'),
    path('plots/add/', plot_add, name='plot-add'),
    path('plots/edit/<int:pk>/', plot_edit, name='plot-edit'),
    path('plots/delete/<int:pk>/', plot_delete, name='plot-delete'),
    path('<int:pk>/map/', farm_map, name='farm-map'),

]
