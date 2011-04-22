from django.conf.urls.defaults import *

from django.contrib import admin

from wes_cms import urls as wes_cms_urls

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    (r'^admin/', include(admin.site.urls)),

    (r'', include(wes_cms_urls)),
)
