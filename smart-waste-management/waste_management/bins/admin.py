from django.contrib import admin
from .models import WasteBin

@admin.register(WasteBin)
class WasteBinAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'bin_type', 'location', 'current_status', 'last_collected')
    list_filter = ('bin_type', 'current_status')
    search_fields = ('identifier', 'location')
