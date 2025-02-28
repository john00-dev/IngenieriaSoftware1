from django.urls import path
from .views import login_redirect, login_page

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('auth/login/', login_redirect, name='login_redirect'),
]
