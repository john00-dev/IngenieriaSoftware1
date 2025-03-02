from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def login_page(request):  
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)  # Iniciar sesión automáticamente
            return redirect('/api/homepatients')  # Redirigir al usuario autenticado
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    
    return render(request, 'authentication/login.html')


def register_page(request):
    return render(request, 'authentication/register.html')


def login_redirect(request):
    return render(request, 'transitions/redirect-to-login.html')


def logout_view(request):
    return render(request, "authentication/logout.html")


@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)  # Autentica al usuario
            if user:
                login(request, user)  # Inicia sesión automáticamente
                return redirect('/api/patients')  # Redirige al usuario autenticado
    
    return render(request, 'authentication/signup.html')
