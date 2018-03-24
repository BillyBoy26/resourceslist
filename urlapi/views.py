from rest_framework.views import APIView
from rest_framework.response import Response

from requests_html import HTMLSession

from linkslist.models import FolderAwe
from linkslist.serializers import LinkSerializer
from urlapi.serializers import serializeHtml


def createLinkData(urldatas):
    link = LinkSerializer(data=urldatas)
    if link.is_valid():
        link.create(link.validated_data)


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
    createLinkData(urldatas)
    if 'imageurl' in urldatas:
        setLinkImageToFolderIfNone(folder, urldatas['imageurl'])
    return urldatas


class HTMLParser(APIView):
    def post(self, request, format=None):
        # TODO clean url
        url = request.data['url']
        folderid = int(request.data['idfolder'])
        folder = FolderAwe.objects.get(id=folderid)
        urldatas = fetchUrl(folder, url)

        return Response(urldatas)
