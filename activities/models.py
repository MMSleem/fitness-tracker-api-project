from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import timedelta

class Activity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities'
    )
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()

    def clean(self):
        if self.duration <= timedelta(0):
            raise ValidationError({'duration': 'Duration must be a positive value.'})

        if self.distance is not None and self.distance <= 0:
            raise ValidationError({'distance': 'Distance must be a positive value.'})

        if self.calories_burned is not None and self.calories_burned <= 0:
            raise ValidationError({'calories_burned': 'Calories burned must be a positive value.'})

    def __str__(self):
        total_seconds = self.duration.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        
        if hours >= 1:
            time_display = f"{int(hours)} hours {int(minutes)} minutes"
        else:
            time_display = f"{int(minutes)} minutes"

        if self.distance is not None:
            distance_meters = self.distance * 1000
            distance_display = f"{distance_meters:.2f} meters"
        else:
            distance_display = "N/A"

        return f"{self.activity_type} by {self.user.email} on {self.date} - Duration: {time_display}, Distance: {distance_display}"
