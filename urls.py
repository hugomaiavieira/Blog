from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos
from tags.models import Tag

blog_dict = {
    'queryset': Artigo.objects.all(),
    'paginate_by': 10,
    'extra_context': {'tags': Tag.objects.all().order_by("nome"), 'artigos': Artigo.objects.all()}
}

urlpatterns = patterns('',

    (r'^$', 'django.views.generic.list_detail.object_list', blog_dict),

    (r'^administration/', include(admin.site.urls)),

    (r'^blog/$', 'django.views.generic.list_detail.object_list', blog_dict),

    (r'blog/artigos/(?P<slug>[\w_-]+)/$', 'blog.views.artigo'),

    (r'^blog/sobre-mim/$', 'blog.views.sobre_mim'),

    (r'^blog/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': {'rss': UltimosArtigos}}),

    (r'^comentarios/', include('django.contrib.comments.urls')),

    (r'tags/', include('tags.urls')),

    (r'^contato/$', 'views.contato'),

    (r'^robots.txt$', 'django.views.static.serve',
     { 'path' : "/robots.txt",
       'document_root': settings.MEDIA_ROOT,
       'show_indexes': False } ),


    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

)

if settings.LOCAL:
    urlpatterns += patterns('',

        (r'^media/(.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)

