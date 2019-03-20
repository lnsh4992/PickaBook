from django.urls import path, re_path

from .views import (
    UserProfileDetailView,
    ProfileDetailView,
    ProfileUpdateView,
    ProfileAddFavView,
    ProfileAddFollowView,
    ProfilePictureView,
    ProfPicV,
    LookupProfileView
)

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('<user__pk>', UserProfileDetailView.as_view(), name='userprofiledetail'),
    path('update/<user__pk>', ProfileUpdateView.as_view()),
    path('user/<pk>', ProfileDetailView.as_view(), name='Profile'),
    re_path(r'^search/(?P<fname>[0-9A-Za-z]+)/(?P<lname>[0-9A-Za-z]+)/$', LookupProfileView.as_view()),
    path('addfavorite/<pk>', ProfileAddFavView.as_view(), name='favoritebook'),
    path('addfollow/<pk>', ProfileAddFollowView.as_view(), name='followauthor'),
    path('resetpw/', PasswordResetView.as_view(), name='reset_password'),
    path('resetpw/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^resetpw/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetpw/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('updatepic/', ProfilePictureView.as_view()),
    path('updatepicprof/<pk>', ProfPicV.as_view())
]