from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

Time_slots=['9 am to 10 am', '10 am to 11 am', '11 am to 12 pm', '2pm to 3pm', '4 pm to 5 pm', '7 pm to 8 pm']


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    name = models.CharField(max_length=100)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=20)
    gender=models.CharField(max_length=6,default='Male')
    location=models.CharField(max_length=15,default='Bangalore')
    #waiting_status=models.BooleanField(default=True)
    date = models.DateField(null=True, blank=True,auto_now_add=True)
    details = models.CharField(max_length=30, default='none')

    '''
    @property
    def is_waiting(self):
        return self.waiting_status
    '''
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,default='Male')
    location = models.CharField(max_length=15,default='Bangalore')
    speciality=models.CharField(max_length=20,default='General medicine')
    years_of_exp=models.IntegerField(default=1)

    def __str__(self):
        return self.name


class DocAvailability(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slots=dict.fromkeys(Time_slots)
    for i in slots:
        slots[i]=models.BooleanField(default=True)


class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField(null=False, blank=False, auto_now_add=True)
    Time_slot=models.CharField(max_length=15)
    is_booked=models.BooleanField(default=False)
    #Timing=models.DateTimeField(default=timezone.now())


@receiver(post_save, sender=Appointment)
def my_handler(sender, instance, **kwargs):
    slot_booked=instance.Time_slot
    doctor=instance.doctor
    DocAvailability(doctor).slots[slot_booked]=False
