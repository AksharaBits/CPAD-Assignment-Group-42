from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='doctor index'),
    path('<int:pk>', views.DoctorDetailView.as_view(), name='doctor_detail'),

    ]