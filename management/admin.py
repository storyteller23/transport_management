from django.contrib import admin
from .models import Transport, Report

# Register your models here.
@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    model = Transport

    list_display = ['name']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    model = Report

    list_display = ['date', 'employee', 'transport', 'fuel_dispended', 'fuel_used', 'mileage']
