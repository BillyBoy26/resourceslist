from rest_framework import generics

from linkslist.models import LinkData, Category, FolderAwe
from linkslist.serializers import LinkSerializer, CategorySerializer, FolderAweSerializer, FolderAweDetailSerializer


class LinkList(generics.ListCreateAPIView):
    queryset = LinkData.objects.all()
    serializer_class = LinkSerializer


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkData.objects.all()
    serializer_class = LinkSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FolderAweList(generics.ListCreateAPIView):
    queryset = FolderAwe.objects.all()
    serializer_class = FolderAweSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.createDefaultCategory(response.data['id'])
        return response

    def createDefaultCategory(self, folderid):
        # TODO on doit surement pouvoir récupérer l'objet FolderAwe avec self sans refaire un appel à la bdd
        if folderid is not None:
            folder = FolderAwe.objects.get(id=folderid)
            if folder is not None:
                Category.objects.create(title="Others", folder=folder)


class FolderAweDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FolderAwe.objects.all()
    serializer_class = FolderAweDetailSerializer
