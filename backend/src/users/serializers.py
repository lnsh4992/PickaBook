from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')