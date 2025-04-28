# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('farm_list')  # Redirect to farm list after login
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'login.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('farm_list')  # Redirect to farm list after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Log the user out
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')  # Redirect to login page after logout