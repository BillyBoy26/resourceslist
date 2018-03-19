from django.contrib import admin

# Register your models here.
from linkslist.models import *


class LinkDataAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "imageurl", "siteurl", "sitename"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "parentcat"]


class ListAwesomeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]


admin.site.register(LinkData, LinkDataAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FolderAwe, ListAwesomeAdmin)
