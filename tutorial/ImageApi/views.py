

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from tutorial.ImageApi.models import Images
from tutorial.ImageApi.serializers import UserSerializer, GroupSerializer, ImagesBasicUserSerializer, \
    ImagesPremiumUserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.none()
    serializer_class = ImagesBasicUserSerializer

    def get_user(self):

        user = self.request.user
        return user

    def get_serializer_class(self):

        user = self.get_user()
        if user.membership == 'Basic':
            return ImagesBasicUserSerializer
        if user.membership == 'Premium':
            return ImagesPremiumUserSerializer

    def get_queryset(self):

        user = self.get_user()
        return Images.objects.filter(author=user)

# Create your views here.
