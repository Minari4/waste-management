# filepath: c:\Users\USER\Desktop\Smart_Waste_Management\smart-waste-management\waste_management\dashboard\urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]