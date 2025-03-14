from django.db import models
from doctors.models import Doctor
from patients.models import Patient
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import path
from django.conf import settings

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),  # Cita disponible para ser reservada
        ('Scheduled', 'Scheduled'),  # Cita ya tomada
        ('Cancelled', 'Cancelled')   # Cita cancelada pero aún en el sistema
    ]
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def cancel_appointment(self):
        """Cancela la cita y la deja disponible para otro paciente."""
        self.status = "Available"
        self.patient = None  # Liberar la cita
        self.save()
    
    def schedule_appointment(self, patient):
        """Programa la cita para un paciente si está disponible."""
        if self.status == "Available":
            self.patient = patient
            self.status = "Scheduled"
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.date} {self.time} - {self.doctor} ({self.status})"


class MedicalNote(models.Model):
    appointment = models.ForeignKey(
        Appointment, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()
