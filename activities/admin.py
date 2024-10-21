from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'duration_hours', 'duration_minutes', 'distance_km', 'distance_meters', 'date')
