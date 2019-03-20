from rest_framework import permissions
from django.shortcuts import get_object_or_404


from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView
)
from users.models import Profile
from .serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
    ProfileAddFavSerializer,
    ProfileAddFollowSerializer
)

# Use to retrieve based on multiple filters
# class MultipleFieldLookupMixin(object):
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """
#     def get_object(self):
#         queryset = self.get_queryset()             # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]: # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#         obj = get_object_or_404(queryset, **filter)  # Lookup the object
#         self.check_object_permissions(self.request, obj)
#         return obj

class UserProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__pk'

class LookupProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        fname = self.kwargs.get('fname')
        lname = self.kwargs.get('lname')
        return Profile.objects.filter(first_name=fname, last_name=lname)[0]

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_field = 'user__pk'

class ProfileAddFavView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileAddFavSerializer

class ProfileAddFollowView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileAddFollowSerializer