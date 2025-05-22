from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import IllegalDumpingReport
from .forms import IllegalDumpingReportForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User

def is_admin(user):
    return user.is_superuser

def is_staff_user(user):
    return user.is_staff and not user.is_superuser

@login_required
@user_passes_test(is_staff_user)
def my_report_list(request):
    # Avoid redirect loop by allowing only staff users to access this view
    if not request.user.is_authenticated or not is_staff_user(request.user):
        return redirect('accounts:login')
    reports = IllegalDumpingReport.objects.filter(user=request.user)
    return render(request, 'reports/my_report_list.html', {'reports': reports})

@login_required
@user_passes_test(is_staff_user)
def my_report_create(request):
    if request.method == 'POST':
        form = IllegalDumpingReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            return redirect('reports:my_report_list')
    else:
        form = IllegalDumpingReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def report_list(request):
    """Only superusers can view the list of all reports"""
    reports = IllegalDumpingReport.objects.all().order_by('-reported_at')
    return render(request, 'reports/report_list.html', {'reports': reports})

@login_required
def report_detail(request, pk):
    """Superusers can view any report, others can only view their own reports"""
    report = get_object_or_404(IllegalDumpingReport, pk=pk)
    if not request.user.is_superuser and report.reporter != request.user:
        messages.error(request, "You don't have permission to view this report.")
        return redirect('dashboard:dashboard')
    return render(request, 'reports/report_detail.html', {'report': report})

@login_required
def report_create(request):
    """Only non-superusers can create reports"""
    if request.user.is_superuser:
        messages.error(request, "Administrators cannot create reports.")
        return redirect('dashboard:dashboard')
    
    if request.method == 'POST':
        form = IllegalDumpingReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            messages.success(request, 'Report submitted successfully!')
            return redirect('dashboard:dashboard')
    else:
        form = IllegalDumpingReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def report_edit(request, pk):
    """Only superusers can edit reports"""
    report = get_object_or_404(IllegalDumpingReport, pk=pk)
    if request.method == 'POST':
        form = IllegalDumpingReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report updated successfully.')
            return redirect('reports:report_detail', pk=pk)
    else:
        form = IllegalDumpingReportForm(instance=report)
    return render(request, 'reports/report_form.html', {'form': form, 'edit_mode': True})

@login_required
@user_passes_test(is_superuser)
def report_delete(request, pk):
    """Only superusers can delete reports"""
    report = get_object_or_404(IllegalDumpingReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'Report deleted successfully.')
        return redirect('reports:report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})
