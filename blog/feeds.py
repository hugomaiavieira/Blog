from django.contrib.syndication.feeds import Feed

from models import Artigo

class UltimosArtigos(Feed):
    title = 'Blog do Hugo Maia Vieira'
    link ='/'

    def items(self):
        return Artigo.objects.all()

