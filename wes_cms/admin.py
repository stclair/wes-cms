from django.contrib import admin
from django import forms
from django.db import models

from images.admin import BaseImageAdmin

from models import Article, Image, NavigationHeader, Navigation

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    list_display = ('slug', 'get_url')

    class Media:
        js = ('/static/js/ckeditor/ckeditor.js',)

class ImageAdmin(BaseImageAdmin):
    list_display = ('listview_thumbnail', 'description', 'image_name', 'get_sample_url')
    exclude = ('serving_url',)

class NavigationHeaderAdmin(admin.ModelAdmin):
    list_display = ('text', 'order')
    ordering = ('order',)

class NavigationAdmin(admin.ModelAdmin):
    list_display = ('text', 'header', 'order', 'article')
    ordering = ('order',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(NavigationHeader, NavigationHeaderAdmin)
admin.site.register(Navigation, NavigationAdmin)