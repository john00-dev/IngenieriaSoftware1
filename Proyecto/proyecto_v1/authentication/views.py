from django.http import HttpResponse
from django.shortcuts import render, redirect

def login_page(request):
    return render(request, 'authentication/login.html')

def login_redirect(request):
    return HttpResponse("¡Has iniciado sesión correctamente!")

def callback_view(request):
    return render(request, "authentication/callback.html")

def logout_view(request):
    return render(request, "authentication/logout.html")
