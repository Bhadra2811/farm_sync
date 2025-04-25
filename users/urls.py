from django.urls import path
from .views import CustomLoginView, manager_dashboard, worker_dashboard, home, custom_logout
from .views import CustomAuthToken
from .views import register


urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('manager/dashboard/', manager_dashboard, name='manager-dashboard'),
    path('worker/dashboard/', worker_dashboard, name='worker-dashboard'),
    path('api/token/', CustomAuthToken.as_view(), name='token-login'),
    path('register/', register, name='register'),
]