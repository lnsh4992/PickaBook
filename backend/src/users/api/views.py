from rest_framework import permissions
from django.shortcuts import get_object_or_404


from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView
)
from users.models import Profile, ProfilePicture
from .serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
    ProfileAddFavSerializer,
    ProfileAddFollowSerializer,
    ProfilePictureSerializer,
    AvatarSerializer
)

from rest_framework.parsers import (
    FileUploadParser,
    FormParser,
    MultiPartParser
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

class ProfilePictureView(CreateAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = AvatarSerializer
    # lookup_field = 'user__pk'
    permission_classes = (permissions.AllowAny,)
    parser_classes = (FormParser, MultiPartParser, FileUploadParser)

    def perform_create(self, serializer):
        print(self.request.FILES['avatar'])
        serializer.save()

class ProfPicV(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePictureSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (FormParser, MultiPartParser, FileUploadParser)

