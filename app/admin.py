from django.contrib import admin
from .models import Patient, AppointmentEmail

admin.site.register(Patient)
admin.site.register(AppointmentEmail)