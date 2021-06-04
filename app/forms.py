from django import forms 
from .models import Patient, AppointmentEmail


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient 
        fields = '__all__'


class AppointmentEmailForm(forms.ModelForm):
    class Meta:
        model = AppointmentEmail
        fields = '__all__'



