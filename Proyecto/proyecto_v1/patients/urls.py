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

urlpatterns = [
    path('homepatients/', PatientHomeView.as_view()),
    path('patients/', ListPatientView.as_view(), name='patients_api'),
    path('patients/<int:pk>/', DetailPatientView.as_view()),
    path('insurances/', ListInsuranceView.as_view()),
    path('insurances/<int:pk>/', DetailInsuranceView.as_view()),
    path('medicalrecords/', ListMedicalRecordView.as_view()),
    path('medicalrecords/<int:pk>/', DetailMedicalRecordView.as_view()),
]
