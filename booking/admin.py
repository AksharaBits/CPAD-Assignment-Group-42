from django.contrib import admin
from .models import Doctor,Patient,Appointment

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ['id', 'name', 'location', 'speciality', 'years_of_exp', ]
    list_editable = ['name', 'location', 'speciality', 'years_of_exp',]
    list_display_links = ['id']


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
