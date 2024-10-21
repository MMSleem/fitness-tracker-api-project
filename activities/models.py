from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

class Activity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities'
    )
    activity_type = models.CharField(max_length=100)
    duration_hours = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99)]
    )
    duration_minutes = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(59)]
    )
    distance_km = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(999)]
    )
    distance_meters = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(999)]  # Max 3 digits for meters
    )
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Activities"

    def clean(self):
        if self.duration_hours < 0:
            raise ValidationError({'duration_hours': 'Hours must be a positive value.'})
        if self.duration_minutes < 0 or self.duration_minutes >= 60:
            raise ValidationError({'duration_minutes': 'Minutes must be between 0 and 59.'})

        if self.distance_km < 0:
            raise ValidationError({'distance_km': 'Kilometers must be a positive value.'})
        if self.distance_meters < 0 or self.distance_meters >= 1000:
            raise ValidationError({'distance_meters': 'Meters must be between 0 and 999.'})

        if self.calories_burned is not None and self.calories_burned <= 0:
            raise ValidationError({'calories_burned': 'Calories burned must be a positive value.'})

    def __str__(self):
        if self.duration_hours >= 1:
            time_display = f"{self.duration_hours} hour{'s' if self.duration_hours != 1 else ''} {self.duration_minutes} minute{'s' if self.duration_minutes != 1 else ''}"
        else:
            time_display = f"{self.duration_minutes} minute{'s' if self.duration_minutes != 1 else ''}"


        if self.distance_km > 0 or self.distance_meters > 0:
            distance_display = f"{self.distance_km} km {self.distance_meters} meters"
        else:
            distance_display = "N/A"

        return f"{self.activity_type} by {self.user.email} on {self.date} - Duration: {time_display}, Distance: {distance_display}"