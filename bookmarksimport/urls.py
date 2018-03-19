from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^importbookmarks/$', views.BookmarkParser.as_view()),
]
