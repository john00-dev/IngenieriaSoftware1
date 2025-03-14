from bookings.views import book_appointment
from django.urls import path
from .views import schedule_appointment_view, cancel_appointment_view
from .views import (
    ListAppointmentView,
    DetailAppointmentView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
    book_appointment,
    create_appointment,
    AppointmentListView,
    AppointmentDoctorListView,
)

urlpatterns = [
    path('appointments/', ListAppointmentView.as_view()),
    path('appointments/<int:pk>/', DetailAppointmentView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
    path('schedule/<int:appointment_id>/', schedule_appointment_view, name='schedule_appointment'),
    path('cancel/<int:appointment_id>/', cancel_appointment_view, name='cancel_appointment'),
    path('create/', create_appointment, name='create_appointment'),
    path('agendar/', book_appointment, name='agendar_cita'),
    path('citas/', AppointmentListView.as_view(), name='citas'),
    path('citasdoctor/', AppointmentDoctorListView.as_view(), name='citasdoctor'),
]

