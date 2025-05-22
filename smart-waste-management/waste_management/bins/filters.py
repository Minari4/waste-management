import django_filters
from django.forms import TextInput, Select
from .models import WasteBin

class WasteBinFilter(django_filters.FilterSet):
    identifier = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Identifier',
        widget=TextInput(attrs={'class': 'form-control'})
    )
    location = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Location',
        widget=TextInput(attrs={'class': 'form-control'})
    )
    bin_type = django_filters.ChoiceFilter(
        choices=WasteBin.BIN_TYPE_CHOICES,
        label='Bin Type',
        widget=Select(attrs={'class': 'form-select'})
    )
    current_status = django_filters.ChoiceFilter(
        choices=WasteBin.STATUS_CHOICES,
        label='Current Status',
        widget=Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = WasteBin
        fields = ['identifier', 'bin_type', 'location', 'current_status']