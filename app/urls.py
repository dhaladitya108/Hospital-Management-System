from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('patient-form/', views.patient_form, name="patient-form"),
    path('patient-list/', views.patient_list, name="patient-list"),
    path('appointment-mail/<patient_email>/', views.appointment_mail, name="appointment-mail"),
]
