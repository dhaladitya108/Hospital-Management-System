from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.messages.constants import WARNING
from django.shortcuts import redirect, render
from django.contrib import messages


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            form = UserCreationForm()
            messages.success(request, 'Account created successfully!')
        else:
            messages.warning(request, 'Looks like something is wrong. Please fill the form correctly')
    context['form']=form
    return render(request,'accounts/sign_up.html',context)