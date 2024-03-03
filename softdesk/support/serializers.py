from django.utils import timezone
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthdate', 'can_be_contacted', 'can_data_be_shared']

    def validate_birthdate(self, value):
        today = timezone.now().date()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 15:
            raise serializers.ValidationError("User must be at least 15 years old")
        return value
