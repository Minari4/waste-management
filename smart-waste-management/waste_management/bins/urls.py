from django.urls import path
from . import views

app_name = 'bins'

urlpatterns = [
    path('', views.bin_list, name='bin_list'),
    path('<int:pk>/', views.bin_detail, name='bin_detail'),
    path('new/', views.bin_create, name='bin_create'),
    path('<int:pk>/edit/', views.bin_edit, name='bin_edit'),  # Edit bin
    path('<int:pk>/delete/', views.bin_delete, name='bin_delete'),  # Delete bin
]