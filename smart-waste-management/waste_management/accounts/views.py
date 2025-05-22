# filepath: c:\Users\USER\Desktop\Smart_Waste_Management\smart-waste-management\waste_management\accounts\views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Successfully logged in!')
        return response

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('dashboard:dashboard')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard:dashboard')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    """View for user profile page"""
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })