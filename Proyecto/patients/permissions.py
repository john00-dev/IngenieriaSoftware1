from rest_framework.permissions import BasePermission
from .models import Patient

class IsPatient(BasePermission):
    """Permiso para permitir solo a los pacientes acceder al endpoint."""

    def has_permission(self, request, view):
        return Patient.objects.filter(email=request.user.email).exists()
