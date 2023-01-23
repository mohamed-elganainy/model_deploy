from .models import Features
from rest_framework import serializers

class features_serializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'