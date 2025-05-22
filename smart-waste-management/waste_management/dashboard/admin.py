from django.contrib import admin
from .models import DashboardWidget  # Replace with your actual model names

@admin.register(DashboardWidget)  # Replace `DashboardWidget` with your model name
class DashboardWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Replace with your model fields
    search_fields = ('name',)
    list_filter = ('created_at',)
