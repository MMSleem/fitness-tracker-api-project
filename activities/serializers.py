from rest_framework import serializers
from .models import Activity
from datetime import timedelta

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ('user',)
    def validate_duration(self, value):
        if value <= timedelta(0):
            raise serializers.ValidationError("Duration must be a positive value.")
        return value

    def validate_distance(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Distance must be a positive value.")
        return value

    def validate_calories_burned(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Calories burned must be a positive value.")
        return value