# filepath: c:\Users\USER\Desktop\Smart_Waste_Management\smart-waste-management\waste_management\routes\urls.py
from django.urls import path
from . import views

app_name = 'routes'

urlpatterns = [
    path('', views.route_list, name='route_list'),
    path('new/', views.route_create, name='route_create'),
    path('<int:pk>/', views.route_detail, name='route_detail'),
    path('<int:pk>/edit/', views.route_edit, name='route_edit'),
    path('<int:pk>/delete/', views.route_delete, name='route_delete'),
]
