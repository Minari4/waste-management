import django_tables2 as tables
from .models import WasteBin
from django.utils.html import format_html

class WasteBinTable(tables.Table):
    identifier = tables.Column(linkify=True)
    current_status = tables.Column(empty_values=())
    
    def render_current_status(self, value, record):
        status_class = {
            'empty': 'success',
            'half': 'warning',
            'full': 'danger',
            'overflow': 'secondary'
        }.get(record.current_status, 'secondary')
        
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            status_class,
            record.get_current_status_display()
        )
    
    class Meta:
        model = WasteBin
        template_name = "django_tables2/bootstrap5.html"
        fields = ('identifier', 'bin_type', 'location', 'current_status', 'last_collected')
        attrs = {
            'class': 'table table-hover',
            'thead': {
                'class': 'table-light'
            }
        }