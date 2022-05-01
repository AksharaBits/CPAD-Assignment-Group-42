from django.contrib import admin
from .models import User, Patient, Doctor, Appointment


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality')
    list_filter = ['speciality']
    search_fields = ['name', 'speciality']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'Time_slot', 'doctor', 'patient', 'is_booked')

    list_filter = ['Time_slot', 'date']

    search_fields = ['Time_slot', 'date']


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment,AppointmentAdmin)