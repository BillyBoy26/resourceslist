from django.contrib.auth.models import User
from requests import Response
from rest_framework import generics

from linkslist.models import LinkData, Category, FolderAwe
from linkslist.serializers import LinkSerializer, CategorySerializer, FolderAweSerializer, FolderAweDetailSerializer, \
    UserSerializer


class LinkList(generics.ListCreateAPIView):
    queryset = LinkData.objects.all()
    serializer_class = LinkSerializer


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkData.objects.all()
    serializer_class = LinkSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        self.update_children(instance)
        self.delete_links(instance)
        return self.destroy(request, *args, **kwargs)

    def delete_links(self, instance):
        LinkData.objects.filter(category=instance.id).delete()

    def update_children(self, catToDelete):
        children = Category.objects.filter(parentcat=catToDelete.id)
        for child in children:
            child.parentcat = catToDelete.parentcat
            child.save()


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


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
