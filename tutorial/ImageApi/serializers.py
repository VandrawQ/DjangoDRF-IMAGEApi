from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tutorial.ImageApi.models import Images


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ImagesBasicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('author', 'title', 'image_200')


class ImagesPremiumUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ('author', 'title', 'image_200', 'image_400', 'image')