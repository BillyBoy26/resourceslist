from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^links/$', views.LinkList.as_view()),
    url(r'^links/(?P<pk>[0-9]+)$', views.LinkDetail.as_view()),
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view()),
    url(r'^folders/$', views.FolderAweList.as_view()),
    url(r'^folders/(?P<pk>[0-9]+)$', views.FolderAweDetail.as_view()),
]
