from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Patient,Doctor

class PatientSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender=forms.CharField(required=True)
    location = forms.CharField(required=True)
    date = forms.DateField()
    details = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.name = self.cleaned_data.get('name')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.name=self.cleaned_data.get('name')
        patient.age=self.cleaned_data.get('age')
        patient.gender=self.cleaned_data.get('gender')
        patient.location=self.cleaned_data.get('location')
        patient.date = self.cleaned_data.get('date')
        patient.details= self.cleaned_data.get('details')
        patient.save()
        return user


class DoctorSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    speciality = forms.CharField(required=True)
    gender = forms.CharField(required=True)
    location = forms.CharField()
    years_of_exp = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.name = self.cleaned_data.get('name')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.name = self.cleaned_data.get('name')
        doctor.speciality=self.cleaned_data.get('speciality')
        doctor.years_of_exp=self.cleaned_data.get('years_of_exp')
        doctor.gender = self.cleaned_data.get('gender')
        doctor.location = self.cleaned_data.get('location')
        doctor.save()
        return user
