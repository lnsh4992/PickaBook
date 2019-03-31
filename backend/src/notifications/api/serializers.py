from rest_framework import serializers
from notifications.models import Notification
from users.api.serializers import ProfileShortSerializer

class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('pk', 'text', 'creation_date', 'prof', 'book', 'question', 'isBook')


