from django.conf.urls.defaults import *

from models import Article, NavigationHeader

nav_headers = NavigationHeader.objects.all()

urlpatterns = patterns('',
    (r'^(?P<slug>[\w-]+)/$', 'django.views.generic.list_detail.object_detail', {'queryset': Article.objects.all(), 'extra_context': {'nav_headers': nav_headers}}),
    (r'', 'wes_cms.views.index')
)
