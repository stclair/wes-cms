from django.conf.urls.defaults import *

from models import Article, Navigation

nav_headers = Navigation.objects.filter(parent=None).order_by('order')

urlpatterns = patterns('',
    url(r'sitemap', 'wes_cms.views.sitemap', name='sitemap'),
    (r'^(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', {'queryset': Article.objects.all(), 'extra_context': {'nav_headers': nav_headers}}),
    (r'', 'wes_cms.views.index')
)
