from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^urldatas/$', views.HTMLParser.as_view()),
]
