from django.urls import path

from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
    DoctorHomeView,
)
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet
from . import views

router = DefaultRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = [
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('create/', views.create_doctor, name='create_doctor'),  # Vista para crear doctores
    path('homedoctors/', DoctorHomeView.as_view()),
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:id>/', DetailDepartmentView.as_view()),
    path('doctoravailabilities/', ListDoctorAvailabilityView.as_view()),
    path('doctoravailabilities/<int:id>/', DetailDoctorAvailabilityView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
] + router.urls
