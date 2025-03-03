from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):  # Extiende el modelo User
    ROLE_CHOICES = [
        ('patient', 'Paciente'),
        ('doctor', 'Doctor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')


