# wigs/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Wig

class WigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wig
        fields = '__all__'

class CustomizeWigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wig
        fields = ['custom_color', 'custom_length', 'custom_curl_pattern', 'custom_density', 'custom_hair_origin']

class PurchaseWigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wig
        fields = []  
        read_only_fields = ['purchaser']

class SwitchUserSerializer(serializers.Serializer):
    username = serializers.CharField()
