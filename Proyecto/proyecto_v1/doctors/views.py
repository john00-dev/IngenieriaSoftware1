from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Doctor,
    Department,
    DoctorAvailability,
    MedicalNote,
)
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Doctor

def register_doctor(request):
    id_number = request.GET.get('id')  # Obtener la cédula del query param
    return render(request, 'authentication/register_doctor.html', {'id_number': id_number})

def create_doctor(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        qualification = request.POST.get('qualification')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        biography = request.POST.get('biography')

        # Crear el doctor en la base de datos
        try:
            Doctor.objects.create(
                id=id,
                first_name=first_name,
                last_name=last_name,
                qualification=qualification,
                contact_number=contact_number,
                email=email,
                address=address,
                biography=biography,
            )
            messages.success(request, 'Doctor registrado con éxito.')
            return redirect('/api/homedoctors')  # Redirigir a la página principal
        except Exception as e:
            messages.error(request, f'Error al registrar doctor: {str(e)}')
            return redirect('register_doctor')  # Redirigir de nuevo al formulario

    # Si no es una solicitud POST, redirigir al formulario de registro
    return redirect('register_doctor')

class DoctorHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'doctors/doctors_home.html'
    permission_classes = [IsAuthenticated]
    login_url = '/auth/login'

class ListDoctorView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
