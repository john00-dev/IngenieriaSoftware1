from django.test import TestCase
from datetime import date
from .models import Patient, Insurance, MedicalRecord

class PatientModelsTest(TestCase):
    
    def setUp(self):
        # Datos iniciales
      
        self.patient = Patient.objects.create(
            first_name="Juan",
            last_name="Velásquez",
            date_of_birth=date(1990, 5, 20),
            contact_number="3204567890",
            email="juan.velasquez@example.com",
            address="Calle 45 #10-23, Bogotá",
            medical_history="Paciente con antecedentes de hipertensión."
        )
        
        self.insurance = Insurance.objects.create(
            patient=self.patient,
            provider="Seguro Salud Plus",
            policy_number="ABC123456",
            expiration_date=date(2026, 12, 31)
        )
        
        self.medical_record = MedicalRecord.objects.create(
            patient=self.patient,
            date=date(2025, 2, 25),
            diagnosis="Gripe común",
            treatment="Reposo e hidratación",
            follow_up_date=date(2025, 3, 5)
        )
    
    def test_patient(self):
        # Verifica que el paciente se creó correctamente
        patient = Patient.objects.get(email="juan.velasquez@example.com")
        self.assertEqual(patient.first_name, "Juan")
        self.assertEqual(patient.last_name, "Velásquez")
        self.assertEqual(patient.medical_history, "Paciente con antecedentes de hipertensión.")
    
    def test_insurance(self):
        # Verifica que el seguro se registró correctamente
        insurance = Insurance.objects.get(patient=self.patient)
        self.assertEqual(insurance.provider, "Seguro Salud Plus")
        self.assertEqual(insurance.policy_number, "ABC123456")
        self.assertEqual(insurance.expiration_date, date(2026, 12, 31))
    
    def test_medical_record(self):
        # Verifica que el historial médico se guarda correctamente
        record = MedicalRecord.objects.get(patient=self.patient)
        self.assertEqual(record.diagnosis, "Gripe común")
        self.assertEqual(record.treatment, "Reposo e hidratación")
        self.assertEqual(record.follow_up_date, date(2025, 3, 5))

# Create your tests here.
