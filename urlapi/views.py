from rest_framework.views import APIView
from rest_framework.response import Response

from requests_html import HTMLSession

from linkslist.serializers import LinkSerializer
from urlapi.serializers import serializeHtml


def createLinkData(urldatas):
    link = LinkSerializer(data=urldatas)
    if link.is_valid():
        link.create(link.validated_data)


class HTMLParser(APIView):
    def post(self, request, format=None):
        # TODO clean url
        url = request.data['url']
        idFolder = request.data['idfolder']

        r = HTMLSession().get(url)
        urldatas = serializeHtml(r)

        urldatas['siteurl'] = url
        urldatas['folder'] = int(idFolder)
        createLinkData(urldatas)

        return Response(urldatas)
