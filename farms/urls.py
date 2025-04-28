from django.urls import path
from . import views

urlpatterns = [
    path('', views.farm_list, name='farm_list'),  # List all farms
    path('<int:farm_id>/', views.farm_detail, name='farm_detail'),  # Farm details
    path('dashboard/', views.dashboard, name='dashboard'),  # Manager dashboard
]