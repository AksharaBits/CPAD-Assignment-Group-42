from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from accounts.models import User,Doctor,Patient,Appointment


# Create your views here.
class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = '../templates/doctor_detail.html'
    context_object_name = 'doctor'


class IndexView(generic.ListView):
    model = Doctor
    template_name = '../templates/doctor_list_index.html'
    context_object_name = 'doctors_list'

    def get_queryset(self):
        return Doctor.objects.all()


def index_page(request):
    specialization_list = Doctor.objects.order_by('speciality').distinct()
    doctors_list = Doctor.objects.all()
    index_page_data = {
        'specialization_list': specialization_list,
        'doctors_list': doctors_list
    }

    return render(request, '../templates/doctor_list_index.html', index_page_data)

