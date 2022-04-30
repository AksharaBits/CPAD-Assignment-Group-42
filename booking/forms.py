from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from booking.models import Patient, Doctor, User

class PatientSignUpForm(UserCreationForm):
    name=forms.CharField()
    age = forms.NumberInput()
    location=forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.name.add(*self.cleaned_data.get('name'))
        patient.age.add(*self.cleaned_data.get('age'))
        patient.location.add(*self.cleaned_data.get('location'))
        return user


class DoctorSignUpForm(UserCreationForm):
    name = forms.CharField()
    speciality = forms.CharField()
    location = forms.CharField()
    years_of_exp=forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor= True
        user.save()
        doctor = Doctor.objects.create(user=user)

        doctor.name.add(*self.cleaned_data.get('name'))
        doctor.years_of_exp.add(*self.cleaned_data.get('years_of_exp'))
        doctor.location.add(*self.cleaned_data.get('location'))
        doctor.speciality.add(*self.cleaned_data.get('speciality'))
        return user