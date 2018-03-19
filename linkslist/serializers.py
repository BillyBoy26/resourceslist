from rest_framework import serializers

from linkslist.models import LinkData, Category, FolderAwe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parentcat')


class FolderAweSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkData
        fields = ('id', 'title', 'description', 'imageurl',
                  'siteurl', 'sitename', 'category', 'folder')
