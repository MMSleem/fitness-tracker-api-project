from django.db import models
from django.conf import settings

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'),
        # Add more as needed
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activities'
    )
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField()  # In minutes
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.email} on {self.date}"
