from django.urls import path

from .views import (
    ListPatientView,
    DetailPatientView,
    ListInsuranceView,
    DetailInsuranceView,
    ListMedicalRecordView,
    DetailMedicalRecordView,
    PatientHomeView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choose_register/', views.choose_register, name='choose_register'),
    path('register_patient/', views.register_patient, name='register_patient'),
    path('create_patient/', views.create_patient, name='create_patient'),  # Vista para crear pacientes
    path('homepatients/', PatientHomeView.as_view()),
    path('patients/', ListPatientView.as_view(), name='patients_api'),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
    path('insurances/', ListInsuranceView.as_view()),
    path('insurances/<int:pk>/', DetailInsuranceView.as_view()),
    path('medicalrecords/', ListMedicalRecordView.as_view()),
    path('medicalrecords/<int:pk>/', DetailMedicalRecordView.as_view()),
]
