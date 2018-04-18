from rest_framework.views import APIView
from rest_framework.response import Response

from requests_html import HTMLSession

from linkslist.models import FolderAwe, Category
from linkslist.serializers import LinkSerializer
from urlapi.serializers import serializeHtml


def createLinkData(urldatas):
    link = LinkSerializer(data=urldatas)
    if link.is_valid():
        link.save()
    return link


def setLinkImageToFolderIfNone(folder, imageurl):
    if not folder.imageurl:
        folder.imageurl = imageurl
        folder.save()


def fetchUrl(folder, url, category):
    print('fetch url ' + url)
    r = HTMLSession().get(url, timeout=30)
    urldatas = serializeHtml(r)
    urldatas['siteurl'] = url
    urldatas['category'] = category.id
    link = createLinkData(urldatas)
    if 'imageurl' in urldatas:
        setLinkImageToFolderIfNone(folder, urldatas['imageurl'])
    return link


class HTMLParser(APIView):
    def post(self, request, format=None):
        # TODO clean url
        url = request.data['url']
        folderId = int(request.data['folderId'])
        categoryId = int(request.data['categoryId'])
        folder = FolderAwe.objects.get(id=folderId)
        category = Category.objects.get(id=categoryId)
        createdLink = fetchUrl(folder, url, category)

        return Response(createdLink.data)
