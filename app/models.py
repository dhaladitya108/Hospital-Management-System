from django.db import models
from django.urls import reverse

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

    