from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Doctor(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(0),  # Asegura que el valor no sea negativo
            MaxValueValidator(9999999999)  # Asegura que el valor no exceda 10 dígitos
        ]
    )  # id manual (tratado como cédula, solo números)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.BigIntegerField(
        validators=[
            MinValueValidator(0),  # Asegura que el valor no sea negativo
            MaxValueValidator(9999999999)  # Asegura que el valor no exceda 10 dígitos
        ]
    )  # Teléfono (solo números)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()
    is_on_vacation = models.BooleanField(default=False)

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='availabilities', on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class MedicalNote(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()