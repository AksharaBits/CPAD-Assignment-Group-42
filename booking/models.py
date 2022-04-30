from typing import Type

from django.db import models
from django.utils import timezone
from django.db.models import IntegerField
from django.contrib.auth.models import AbstractUser
# Create your models here.


# User class
class User(AbstractUser):
    # Define the extra fields
    # related to User here
    first_name = models.CharField('First Name of User',
                                  blank=True, max_length=20)
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)
    # More User fields according to need
'''
    # define the custom permissions
    # related to User.
    class Meta:
        permissions = (('book_appointment','view_appointments'), ('view_patient_history','view_appointments'))
'''

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=20)
    gender=models.CharField(max_length=6,default='Male')
    location=models.CharField(max_length=15,default='Bangalore')
    waiting_status=models.BooleanField(default=True)

    @property
    def is_waiting(self):
        return self.waiting_status

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,default='Male')
    location = models.CharField(max_length=15,default='bangalore')
    speciality=models.CharField(max_length=20,default='General medicine')
    years_of_exp=models.IntegerField(default=1)

    def __str__(self):
        return self.name


class PatientHistory(models.Model):
    id=models.OneToOneField(Patient,primary_key=True, on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now())
    details=models.CharField(max_length=30,default='none')


class Appointment(models.Model):
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    #Timing=models.DateTimeField(default=timezone.now())


class Medicine(models.Model):
    name=models.CharField(max_length=20)
    cost=models.IntegerField()