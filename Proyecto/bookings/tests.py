from django.test import TestCase
from datetime import date, time
from doctors.models import Doctor
from patients.models import Patient
from .models import Appointment, MedicalNote


class AppointmentModelsTest(TestCase):
    
    def setUp(self):
        # Configura los datos iniciales para las pruebas
        self.patient = Patient.objects.create(
            first_name="Juan",
            last_name="Pérez",
            date_of_birth=date(1990, 5, 15),
            contact_number="3101234567",
            email="juan.perez@example.com",
            address="Carrera 12 #34-56, Bogotá"
        )
        
        self.doctor = Doctor.objects.create(
            first_name="Laura",
            last_name="Gómez",
            qualification="Médico General",
            contact_number="3209876543",
            email="laura.gomez@clinic.com",
            address="Avenida Siempre Viva 742",
            biography="Médico general con amplia experiencia en consultas de atención primaria.",
            is_on_vacation=False
        )
        
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_date=date(2025, 4, 10),
            appointment_time=time(10, 30),
            notes="Consulta de seguimiento para control de presión arterial.",
            status="Pendiente"
        )
        
        self.medical_note = MedicalNote.objects.create(
            appointment=self.appointment,
            note="Paciente presenta presión arterial dentro de valores normales. Se recomienda continuar con la medicación.",
            date=date(2025, 4, 10)
        )
        
    def test_appointment_creation(self):
        # Verifica que la cita se creó correctamente
        appointment = Appointment.objects.get(patient=self.patient)
        self.assertEqual(appointment.doctor, self.doctor)
        self.assertEqual(appointment.status, "Pendiente")
        
    def test_medical_note_creation(self):
        # Verifica que la nota médica se guarda correctamente
        note = MedicalNote.objects.get(appointment=self.appointment)
        self.assertIn("presión arterial dentro de valores normales", note.note)
        self.assertEqual(note.date, date(2025, 4, 10))

# Create your tests here.
