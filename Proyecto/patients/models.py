from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(0),  # Asegura que el valor no sea negativo
            MaxValueValidator(9999999999)  # Asegura que el valor no exceda 10 dígitos
        ]
    )  # id manual (tratado como cédula, solo números)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()


class Insurance(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='insurances', on_delete=models.CASCADE
    )
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiration_date = models.DateField()


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, related_name='medical_records', on_delete=models.CASCADE
    )
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    follow_up_date = models.DateField()
