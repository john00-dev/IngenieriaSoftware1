from django.urls import path

from .views import ( 
    login_page, 
    logout_view,
    register_page,
    signup,
    choose_register,
)

urlpatterns = [
    path('choose_register/', choose_register, name='choose_register'),
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_view, name='logout'),
]
