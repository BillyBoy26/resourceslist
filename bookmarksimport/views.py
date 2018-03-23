# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup, SoupStrainer
import time

from linkslist.models import Category, FolderAwe, LinkData


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

        defaultCategory = Category.objects.create(title="Others", folder=folder)

        self.processElement(dl, defaultCategory)

        return Response()

    def processElement(self, element, parentcat):
        print('dl')
        linkChildrens = element.findChildren(['a'], recursive=False)
        if linkChildrens:
            for child in linkChildrens:
                self.processLink(child, parentcat)
        childrens = element.findChildren(['h3', 'dl'], recursive=False)
        if childrens:
            currentCat = parentcat
            for child in childrens:
                balise = child.name
                if balise == 'h3':
                    currentCat = self.processCat(child, parentcat)
                elif balise == 'dl':
                    self.processElement(child, currentCat)

    def processCat(self, element, parentcat):
        cat = self.saveCategory(element, parentcat)
        print('create category ' + cat.title)
        return cat

    def processLink(self, element, category):
        link = self.saveLink(element, category)
        print('create link ' + link.title + ' with category ' + category.title)

    def saveLink(self, row, category):
        uri = row['href']
        title = row.contents[0]
        createdate = time.ctime(int(row['add_date']))
        link = LinkData()
        link.title = title
        link.siteurl = uri
        link.category = category
        link.save()
        return link

    def saveCategory(self, row, parentcat=None):
        cat = Category()
        cat.title = row.text
        cat.folder = self.folder
        cat.parentcat = parentcat
        cat.save()
        return cat
