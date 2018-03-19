
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class BookmarkParser(APIView):
    def post(self, request, format=None):
        # TODO clean url
        bookmarkFile = request.data['bookmarks']

        return Response()
