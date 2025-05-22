from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class WasteBin(models.Model):
    BIN_TYPE_CHOICES = [
        ('recyclable', 'Recyclable'),
        ('organic', 'Organic'),
        ('general', 'General'),
    ]

    STATUS_CHOICES = [
        ('empty', 'Empty'),
        ('half', 'Half Full'),
        ('full', 'Full'),
    ]

    identifier = models.CharField(max_length=100, unique=True)
    bin_type = models.CharField(max_length=20, choices=BIN_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    current_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='empty')
    last_collected = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['identifier']
        verbose_name = 'Waste Bin'
        verbose_name_plural = 'Waste Bins'

    def __str__(self):
        return f"{self.identifier} - {self.get_bin_type_display()}"

    def get_absolute_url(self):
        return reverse('bins:bin_detail', args=[str(self.id)])

    def get_bin_type_display(self):
        return dict(self.BIN_TYPE_CHOICES).get(self.bin_type, self.bin_type)

    def get_current_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.current_status, self.current_status)