# Create your views here.
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView

from linkslist.models import Category, FolderAwe
from urlapi.views import fetchUrl
from requests.exceptions import ConnectionError


class BookmarkParser(APIView):
    def __init__(self):
        self.folder = {}

    def post(self, request, format=None):
        # TODO test file
        bookmarkFile = request.data['bookmarks']

        html = bookmarkFile.read().decode().replace('<DT>', '').replace('<p>', '').replace('</p>', '')
        bookmarkFile.close()
        soup = BeautifulSoup(html, "html")
        print(soup.prettify())

        dl = soup.find('dl')
        # TODO send error if file is bad
        if not dl:
            raise ValueError('nothing to import')

        folder = FolderAwe()
        folder.title = "Favoris"
        folder.description = "Import des favoris"
        folder.save()
        self.folder = folder

        self.processElement(dl)

        return Response()

    def processElement(self, element, parentcat=None):
        linkChildrens = element.findChildren(['a'], recursive=False)
        if linkChildrens:
            for child in linkChildrens:
                self.saveLink(child, parentcat)
        childrens = element.findChildren(['h3', 'dl'], recursive=False)
        if childrens:
            currentCat = parentcat
            for child in childrens:
                balise = child.name
                if balise == 'h3':
                    currentCat = self.saveCategory(child, parentcat)
                elif balise == 'dl':
                    self.processElement(child, currentCat)

    def saveLink(self, row, category):
        uri = row['href']
        try:
            fetchUrl(self.folder, uri, category)
        except ConnectionError:
            print('Connection error with ' + uri)

    def saveCategory(self, row, parentcat=None):
        cat = Category()
        cat.title = row.text
        cat.folder = self.folder
        cat.parentcat = parentcat
        cat.save()
        return cat
