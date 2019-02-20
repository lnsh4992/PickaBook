from django.urls import path, re_path

from .views import (
    ProfileDetailView,
    ProfileUpdateView
)

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('<user__pk>', ProfileDetailView.as_view()),
    path('update/<user__pk>', ProfileUpdateView.as_view()),
    path('resetpw/', PasswordResetView.as_view(), name='reset_password'),
    path('resetpw/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^resetpw/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetpw/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]