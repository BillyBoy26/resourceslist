from django.db import models


class FolderAwe(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    author = models.TextField()
    createdate = models.DateField(auto_now_add=True)


class Category(models.Model):
    title = models.TextField()
    parentcat = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    folder = models.ForeignKey(FolderAwe, on_delete=models.CASCADE, related_name='categories')


class LinkData(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    imageurl = models.TextField(blank=True)
    siteurl = models.TextField()
    sitename = models.CharField(max_length=100, blank=True)
    createdate = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='links')
