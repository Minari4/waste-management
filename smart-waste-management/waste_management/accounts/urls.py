# filepath: c:\Users\USER\Desktop\Smart_Waste_Management\smart-waste-management\waste_management\accounts\urls.py
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, signup_view, profile_view

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
]