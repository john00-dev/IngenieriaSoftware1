from django.urls import path

from .views import (
    login_redirect, 
    login_page, 
    logout_view,
    register_page,
    signup,
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('redirect/', login_redirect, name='login_redirect'),
    path('logout/', logout_view, name='logout'),
]
