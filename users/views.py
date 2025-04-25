from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from farm.models import Farm, Plot
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .forms import UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        user = self.request.user
        if user.role == 'manager':
            return reverse_lazy('manager-dashboard')
        elif user.role == 'worker':
            return reverse_lazy('worker-dashboard')
        return reverse_lazy('login')
   
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
            'role': token.user.role
        })

@login_required
def manager_dashboard(request):
    farms = Farm.objects.filter(owner=request.user)
    plots = Plot.objects.filter(farm__owner=request.user)
    total_farms = farms.count()
    total_plots = plots.count()
    total_crops = plots.exclude(crop_type='').count()  # optional
    recent_farms = farms.order_by('-id')[:5]
    recent_plots = plots.order_by('-id')[:5]
    context = {
        'total_farms': total_farms,
        'total_plots': total_plots,
        'total_crops': total_crops,
        'recent_farms': recent_farms,
        'recent_plots': recent_plots,
    }
    return render(request, 'users/manager_dashboard.html', context)

@login_required
def worker_dashboard(request):
    return render(request, 'users/worker_dashboard.html')

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'manager':
            return redirect('manager-dashboard')
        elif request.user.role == 'worker':
            return redirect('worker-dashboard')
    return render(request, 'users/home.html')

def register(request):
    # Clear any logout messages first
    storage = messages.get_messages(request)
    new_messages = []
    for message in storage:
        if 'logged out' not in str(message).lower():
            new_messages.append(message)
    storage.used = True
    
    # Re-add messages that weren't about logging out
    for message in new_messages:
        messages.add_message(request, message.level, message.message)
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            if user.role == 'manager':
                return redirect('manager-dashboard')
            else:
                return redirect('worker-dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')