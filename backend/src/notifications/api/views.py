from rest_framework import permissions
from django.shortcuts import get_object_or_404


from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView
)

from notifications.models import Notification
from .serializers import (
    NotificationCreateSerializer,
)

class NotificationCreateView(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateSerializer

class NotificationDestroyView(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateSerializer

class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateSerializer

    def get_queryset(self):
        return Notification.objects.filter(prof=self.kwargs['fk']).order_by('creation_date')
