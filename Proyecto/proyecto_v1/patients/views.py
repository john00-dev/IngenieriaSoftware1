from django.views.generic import TemplateView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated

class PatientHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'patients/patient_home.html'
    permission_classes = [IsAuthenticated]
    login_url = '/auth/login'


class ListPatientView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ListInsuranceView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class ListMedicalRecordView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
