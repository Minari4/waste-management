from django.contrib import admin
from .models import CollectionRoute, RouteBin
from django import forms

class RouteBinInline(admin.TabularInline):
    model = RouteBin
    extra = 1
    fields = ('bin', 'collection_order')
    ordering = ('collection_order',)

class CollectionRouteAdminForm(forms.ModelForm):
    class Meta:
        model = CollectionRoute
        fields = '__all__'

@admin.register(CollectionRoute)
class CollectionRouteAdmin(admin.ModelAdmin):
    form = CollectionRouteAdminForm
    list_display = ('name', 'assigned_to', 'collection_day', 'is_active')
    list_filter = ('is_active', 'collection_day', 'assigned_to')
    search_fields = ('name', 'description')
    inlines = [RouteBinInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'assigned_to', 'collection_day', 'is_active')
        }),
        ('Route Coordinates', {
            'fields': (
                ('point_a_latitude', 'point_a_longitude'),
                ('point_b_latitude', 'point_b_longitude')
            )
        }),
    )