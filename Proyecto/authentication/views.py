from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import CustomUser  # Asegúrate de que estás usando tu modelo personalizado

User = get_user_model()  # Usar el modelo personalizado

# Vistas para renderizar templates HTML
def signup(request):
    if request.method == "POST":
        id_number = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  # "patient" o "doctor"

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
        else:
            user = CustomUser.objects.create_user(id=id_number, username=username, password=password, role=role)
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                # Generar y guardar el token de autenticación
                token, created = Token.objects.get_or_create(user=user)
                request.session['token'] = token.key

                if role == "patient":
                    return redirect(f'/api/register_patient/?id={id_number}')  # Redirigir con ID
                else:
                    return redirect(f'/api/register_doctor/?id={id_number}')  # Redirigir con ID

    return render(request, 'authentication/signup.html')


def login_page(request):  
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)  # Iniciar sesión automáticamente

            # Generar y guardar el token de autenticación
            token, created = Token.objects.get_or_create(user=user)
            request.session['token'] = token.key
            
            # Verificar el rol del usuario y redirigir según corresponda
            if user.role == "doctor":
                return redirect('/api/homedoctors')
            elif user.role == "patient":
                return redirect('/api/homepatients')
            else:
                messages.error(request, "Rol de usuario no válido.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    
    return render(request, 'authentication/login.html')


def logout_view(request):
    # Eliminar el token de la sesión
    if 'token' in request.session:
        del request.session['token']

    logout(request)
    return redirect('/')


def choose_register(request):
    return render(request, 'authentication/choose_register.html')


def register_page(request):
    return render(request, 'authentication/register.html')



