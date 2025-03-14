from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer

# Vistas para renderizar templates HTML
def register_patient(request):
    id = request.GET.get("id")  # Obtiene el ID de la URL
    print("ID recibido:", id)  # Verifica en la terminal
    return render(request, "authentication/register.html", {"id": id})


def create_patient(request):
    if request.method == "POST":
        id = request.POST['id']  # Recupera la cédula ingresada
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        address = request.POST['address']
        medical_history = request.POST['medical_history']

        # Crear el paciente en la base de datos
        Patient.objects.create(
            id=id,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            contact_number=contact_number,
            email=email,
            address=address,
            medical_history=medical_history
        )

        return redirect('/api/homepatients')  # Redirige a una página de éxito

    return render(request, 'create_patient.html')


def home(request):
    return render(request, 'home.html')


def choose_register(request):
    return render(request, 'choose_register.html')


# Vistas para la API
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
