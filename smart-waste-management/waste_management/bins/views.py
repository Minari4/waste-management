from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig
from .models import WasteBin
from .tables import WasteBinTable
from .forms import WasteBinForm
import json
from django.contrib.auth.decorators import user_passes_test, login_required

def is_superuser(user):
    return user.is_superuser

@login_required
def bin_list(request):
    search_location = request.GET.get('location', '').strip()
    bins = WasteBin.objects.all()
    if search_location:
        bins = bins.filter(location__icontains=search_location)
    table = WasteBinTable(bins)
    RequestConfig(request).configure(table)

    # Define the geographical bounds for Surigao City
    SURIGAO_CITY_BOUNDS = {
        "min_latitude": 9.75,
        "max_latitude": 9.85,
        "min_longitude": 125.45,
        "max_longitude": 125.60,
    }

    # Filter bins within Surigao City bounds
    bins_data = [
        {
            "identifier": bin.identifier,
            "latitude": bin.latitude,
            "longitude": bin.longitude,
            "location": bin.location,
            "status": bin.get_current_status_display(),
            "bin_type": bin.get_bin_type_display(),
        }
        for bin in bins
        if (
            SURIGAO_CITY_BOUNDS["min_latitude"] <= bin.latitude <= SURIGAO_CITY_BOUNDS["max_latitude"]
            and SURIGAO_CITY_BOUNDS["min_longitude"] <= bin.longitude <= SURIGAO_CITY_BOUNDS["max_longitude"]
        )
    ]

    return render(request, 'bins/bin_list.html', {
        'table': table,
        'bins_json': json.dumps(bins_data),  # Pass serialized data to the template
        'search_location': search_location,
    })

@login_required
def bin_detail(request, pk):
    """
    View to display the details of a specific waste bin.
    """
    bin = get_object_or_404(WasteBin, pk=pk)
    return render(request, 'bins/bin_detail.html', {'bin': bin})

@user_passes_test(is_superuser)
def bin_create(request):
    """
    View to create a new waste bin.
    """
    if request.method == 'POST':
        form = WasteBinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bins:bin_list')  # Redirect to the bin list page after saving
    else:
        form = WasteBinForm()
    return render(request, 'bins/bin_form.html', {'form': form})

@user_passes_test(is_superuser)
def bin_edit(request, pk):
    """
    View to edit an existing waste bin.
    """
    bin = get_object_or_404(WasteBin, pk=pk)
    if request.method == 'POST':
        form = WasteBinForm(request.POST, instance=bin)
        if form.is_valid():
            form.save()
            return redirect('bins:bin_list')  # Redirect to the bin list page after saving
    else:
        form = WasteBinForm(instance=bin)
    return render(request, 'bins/bin_form.html', {'form': form, 'edit_mode': True})

@user_passes_test(is_superuser)
def bin_delete(request, pk):
    """
    View to delete a waste bin.
    """
    bin = get_object_or_404(WasteBin, pk=pk)
    if request.method == 'POST':
        bin.delete()
        return redirect('bins:bin_list')  # Redirect to the bin list page after deletion
    return render(request, 'bins/bin_confirm_delete.html', {'bin': bin})
