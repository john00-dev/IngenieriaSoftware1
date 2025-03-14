# Librerías y módulos
from django.http import JsonResponse
from django.shortcuts import render, redirect  # Palfuturo
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

# Modelos y formularios
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer
from bookings.forms import AppointmentForm



# Vistas basadas en clases para la interfaz HTML
class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = "patients/appointment_list.html"  # Ajusta la ruta si es necesario
    context_object_name = "appointments"

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentDoctorListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = "patients/appointment_list.html"
    context_object_name = "appointments"

    def get_queryset(self):
        return Appointment.objects.filter(doctor_id=self.request.user.id)



# Vistas basadas en clases para la API
class ListAppointmentView(ListAPIView, CreateAPIView):
    """
    API para gestionar citas médicas.

    Métodos disponibles:
    - GET: Lista todas las citas médicas programadas.
    - POST: Crea una nueva cita médica.
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


# Vistas basadas en funciones para la API
def schedule_appointment_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if appointment.schedule_appointment(request.user):
        return JsonResponse({"message": "Cita programada exitosamente."})
    return JsonResponse({"error": "No se pudo programar la cita."}, status=400)


def cancel_appointment_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.cancel_appointment()
    return JsonResponse({"message": "Cita cancelada exitosamente."})


# Vistas basadas en funciones para la interfaz HTML
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user  # Asigna el paciente actual
            appointment.save()
            return redirect('/api/homepatients')  # Redirige a una página de éxito
    else:
        form = AppointmentForm()

    return render(request, 'patients/create_appointment.html', {'form': form})


def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')  # Url para listar citas
    else:
        form = AppointmentForm()

    return render(request, 'patients/create_appointment.html', {'form': form})
