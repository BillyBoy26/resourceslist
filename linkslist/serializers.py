from rest_framework import serializers

from linkslist.models import LinkData, Category, FolderAwe


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkData
        fields = ('id', 'title', 'description', 'imageurl',
                  'siteurl', 'sitename', 'category')


class CategorySerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'parentcat', 'links')


class FolderAweDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description', 'categories')


class FolderAweSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderAwe
        fields = ('id', 'title', 'description', 'imageurl', 'createdate', 'updatedate')
