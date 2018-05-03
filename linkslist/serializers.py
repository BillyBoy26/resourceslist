from django.contrib.auth.models import User
from rest_framework import serializers
from urllib.parse import urlparse
from rest_framework import permissions

from linkslist.models import LinkData, Category, FolderAwe


class LinkSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    simpleSiteUrl = serializers.SerializerMethodField('getSimpleUrl')

    def getSimpleUrl(self, obj):
        if obj.siteurl:
            return urlparse(obj.siteurl).netloc
        return ''

    class Meta:
        fields = ('id', 'title', 'description', 'imageurl',
                  'siteurl', 'simpleSiteUrl', 'sitename', 'category', 'createdate')
        model = LinkData


class CategorySerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'parentcat', 'links', 'folder')


class FolderAweDetailSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description', 'categories')


class FolderAweSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description', 'imageurl', 'createdate', 'updatedate')


class UserSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticated,)
    folders = FolderAweSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'folders')
