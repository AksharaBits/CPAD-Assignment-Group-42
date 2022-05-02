from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import PatientSignUpForm, DoctorSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import Doctor,Patient,Appointment


def index(request):
    return render(request, '../templates/index.html')

def register(request):
    return render(request, '../templates/register.html')

def view_patient_history(request):
    patients_list = Doctor.objects.all()
    context_obj={'patients_list': patients_list}
    return render(request, '../templates/patient_history.html', context_obj)


class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = '../templates/patient_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/appointments/')


class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = '../templates/doctor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


