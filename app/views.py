from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientForm, AppointmentEmailForm
from .models import AppointmentEmail, Patient

from django.core.mail import send_mail


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


def appointment_mail(request, patient_email):
    context = {
        'email': patient_email,
    }
    form = AppointmentEmailForm()
    if request.method == 'POST':
        form = AppointmentEmailForm(request.POST)
        if form.is_valid():
            email_appointed = form.save()
            send_mail(
                email_appointed.subject,
                email_appointed.message,
                'testerperson1029@gmail.com',
                [email_appointed.email],
                fail_silently=False
            )
            return redirect('patient-list')
    return render(request, 'app/appointment_mail.html', context)


    # def dispatch_mail(request):
    #     if request.method == 'POST':
    #         email = request.POST.get('email')
    #         message = request.POST.get('subject')
    #         subject = request.POST.get('subjez,c msdmjcmkdmckmdskcct')
    #         print(email, subject, message)
    #
    #
    #
    #         return HttpResponseRedirect(reverse('home'))
    #
    #     else:
    #         return HttpResponse('Invalid request')
