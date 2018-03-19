from rest_framework import generics

from linkslist.models import LinkData, Category, FolderAwe
from linkslist.serializers import LinkSerializer, CategorySerializer, ListAwesomeSerializer


class LinkList(generics.ListCreateAPIView):
    queryset = LinkData.objects.all()
    serializer_class = LinkSerializer


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkData.objects.all()
    serializer_class = LinkSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListAwesomeList(generics.ListCreateAPIView):
    queryset = FolderAwe.objects.all()
    serializer_class = ListAwesomeSerializer
