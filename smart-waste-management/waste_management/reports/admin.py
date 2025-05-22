from django.contrib import admin
from .models import IllegalDumpingReport

@admin.register(IllegalDumpingReport)
class IllegalDumpingReportAdmin(admin.ModelAdmin):
    list_display = ('location', 'status', 'reported_at', 'reporter')
    list_filter = ('status',)
    search_fields = ('location', 'description')
