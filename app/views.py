from django.shortcuts import render
from django.contrib import messages
from .forms import PatientForm
from .models import Patient


def home(request):
    return render(request, 'app/index.html')


def patient_form(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            form = PatientForm()
            messages.success(request, 'Your request has been successfully submitted')
        else:
            messages.warning(request, 'Something went wrong, Please fill the form correctly')
    return render(request, 'app/patient_form.html', {'form': form})


def patient_list(request):
    data = Patient.objects.all()
    return render(request, 'app/patient_list.html', {'datas': data})

