from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404

from models import Artigo
from tags.models import Tag

def artigo(request, slug):
    tags = Tag.objects.all().order_by("nome")
    artigos = Artigo.objects.all()
    artigo = get_object_or_404(Artigo, slug=slug)
    return render_to_response('blog/artigo.html', locals(),
        context_instance=RequestContext(request))

def sobre_mim(request):
    tags = Tag.objects.all().order_by("nome")
    artigos = Artigo.objects.all()
    return render_to_response('blog/sobre-mim.html', locals(),
    context_instance=RequestContext(request))

