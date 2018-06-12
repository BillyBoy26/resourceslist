from math import floor
from rest_framework.views import APIView
from rest_framework.response import Response

from requests_html import HTMLSession

from linkslist.models import FolderAwe, Category
from linkslist.serializers import LinkSerializer
from urlapi.serializers import serializeHtml

from requests.exceptions import ReadTimeout


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
    import time
    start = time.time()

    try:
        r = HTMLSession().get(url, timeout=20)
        urldatas = serializeHtml(r)
        urldatas['siteurl'] = url
        urldatas['category'] = category.id
        link = createLinkData(urldatas)
        if 'imageurl' in urldatas:
            setLinkImageToFolderIfNone(folder, urldatas['imageurl'])
        executionTime = floor((time.time() - start) * 1000)

        print('time ' + str(executionTime) + ' ms')
        return link
    except ConnectionError as e:
        print('Connection error with ' + url)
        raise e
    except ReadTimeout as e:
        print('Read Timeout error with ' + url)
    except Exception as e:
        print('Unknow problem with ' + url)
        print(e)


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
