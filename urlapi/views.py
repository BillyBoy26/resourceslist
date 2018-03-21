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


def setLinkImageToFolderIfNone(folderid, imageurl):
    if imageurl:
        folder = FolderAwe.objects.get(id=folderid)
        if not folder.imageurl:
            folder.imageurl = imageurl
            folder.save()


class HTMLParser(APIView):
    def post(self, request, format=None):
        # TODO clean url
        url = request.data['url']
        folderid = int(request.data['idfolder'])

        r = HTMLSession().get(url)
        urldatas = serializeHtml(r)

        urldatas['siteurl'] = url
        urldatas['folder'] = folderid
        createLinkData(urldatas)
        setLinkImageToFolderIfNone(folderid, urldatas['imageurl'])

        return Response(urldatas)
