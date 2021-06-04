from django.db import models
from django import forms


class Patient(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    phone_number = models.CharField(max_length=10)
    health_condition = models.CharField(max_length=200)
    prescription = models.FileField(upload_to='prescriptions', blank=True, null=True)

    def __str__(self):
        return self.name


class AppointmentEmail(models.Model):
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=60)
    message = models.CharField(max_length=400)

    def __str__(self):
        return self.email
