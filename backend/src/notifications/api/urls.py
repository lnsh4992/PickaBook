from django.urls import path

from .views import (
    NotificationCreateView,
    NotificationListView,
    NotificationDestroyView
)

urlpatterns = [
    path('<fk>', NotificationListView.as_view(), name="notificationlist"),
    path('create/', NotificationCreateView.as_view(), name='createnotification'),
    path('destroy/<pk>', NotificationDestroyView.as_view(), name='destroynotification')
]