from django.contrib import admin
from .models import Measurement

# Register your models here.

class MeasurementAdmin(admin.ModelAdmin):
    list_display="Temperature","Humidity"

admin.site.register(Measurement,MeasurementAdmin)