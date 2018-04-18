from rest_framework import serializers
from urllib.parse import urlparse

from linkslist.models import LinkData, Category, FolderAwe


class LinkSerializer(serializers.ModelSerializer):
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
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'parentcat', 'links', 'folder')


class FolderAweDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description', 'categories')


class FolderAweSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description', 'imageurl', 'createdate', 'updatedate')
