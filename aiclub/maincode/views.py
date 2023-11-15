from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.cache import cache
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required

# Define a custom decorator for rate limiting


def home(request):
    return render(request, 'main_app/home.html')
@login_required
def success_login(request, title=None):
    if title == 1:
        title = "Lab 01: Captcha"
    elif title == 0:
        title = "Lab 00: Brute Force"
    else:
        return HttpResponse("im underwater")

    return render(request, 'main_app/success_login.html', {'title': title})
def login_view(request):
    if request.method == 'POST':
        print(request)
        username = request.POST.get('usernameEmail')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Only call login if user is successfully authenticated
            messages.success(request, 'Login successful.', extra_tags='success')
            return redirect('success_login', title=0)
        else:
            messages.error(request, 'Invalid username or password.', extra_tags='danger')

    return render(request, 'main_app/login.html')

def login_captcha(request):
    if request.method == 'POST':
        print(request)
        username = request.POST.get('usernameEmail')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Only call login if user is successfully authenticated
            return redirect('success_login', title=1)
        else:
            messages.error(request, 'Invalid username or password.', extra_tags='danger')

    return render(request, 'main_app/login_turing.html')

