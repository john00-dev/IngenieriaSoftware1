from django.urls import path

from .views import (
    login_redirect, 
    login_page, 
    callback_view, 
    logout_view,
)

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('redirect/', login_redirect, name='login_redirect'),
    path("callback/", callback_view, name="callback"),
    path('logout/', logout_view, name='logout'),
]
