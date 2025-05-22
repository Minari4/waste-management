# filepath: c:\Users\USER\Desktop\Smart_Waste_Management\smart-waste-management\waste_management\dashboard\views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bins.models import WasteBin
from reports.models import IllegalDumpingReport
from django.core.serializers import serialize
import json
from random import choice

@login_required
def dashboard(request):
    bins = WasteBin.objects.all()
    full_bins = bins.filter(current_status='full')  # Filter bins with 'full' status

    # Environmental reminders
    environmental_reminders = [
        "Reduce, Reuse, Recycle - The three R's of waste management.",
        "Segregate your waste properly to help with recycling efforts.",
        "Plastic takes hundreds of years to decompose. Choose eco-friendly alternatives!",
        "Composting organic waste helps reduce landfill waste and creates nutrient-rich soil.",
        "Report illegal dumping to keep our community clean and safe.",
        "Every small action counts in protecting our environment.",
        "Think before you throw - could this item be recycled or reused?",
        "Clean environment, healthy community - let's work together!",
    ]

    # Serialize bins data for JavaScript
    bins_data = [
        {
            "identifier": bin.identifier,
            "bin_type": bin.get_bin_type_display(),
            "location": bin.location,
            "latitude": bin.latitude,
            "longitude": bin.longitude,
            "current_status": bin.get_current_status_display(),
        }
        for bin in bins if bin.latitude is not None and bin.longitude is not None
    ]

    context = {
        'bins': json.dumps(bins_data),
        'full_bins': full_bins,
        'total_bins': bins.count(),
        'environmental_reminder': choice(environmental_reminders),  # Randomly select a reminder
    }

    # Only add reports to context for superusers
    if request.user.is_superuser:
        reports = IllegalDumpingReport.objects.filter(status='reported').order_by('-reported_at')[:5]
        context['reports'] = reports

    return render(request, 'dashboard/dashboard.html', context)
