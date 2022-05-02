from django.urls import path
from .import views
from appointments import views as appviews
from accounts import views as accviews
from django.contrib import admin

urlpatterns=[
     path('',views.index, name='index'),
     path('appointments/', appviews.index_page, name='doctor index'),
     path('accounts/',accviews.view_patient_history, name='patient history'),
     #path('admin/', admin.site.urls, name='admin'),
]