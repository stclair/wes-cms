from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_detail

from wes_cms.models import Article, Navigation

nav_headers = Navigation.objects.filter(parent=None)

def index(request):
    return object_detail(request, Article.objects.all(),
                         slug=Navigation.objects.get_first().get_article().slug,
                         extra_context={'nav_headers': nav_headers})

def sitemap(request):
    sitemap = []
    for navigation in nav_headers:
        sitemap += navigation.flatten()
    return render_to_response('wes_cms/sitemap.html', {'sitemap': sitemap, 'nav_headers': nav_headers})