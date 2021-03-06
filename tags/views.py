from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from models import Tag
from blog.models import Artigo

def tag(request, tag_nome):
    tags = Tag.objects.all().order_by("nome")
    tag = get_object_or_404(Tag, nome=tag_nome)
    artigos = Artigo.objects.all()
    return render_to_response(
        'tags/tag.html',
        locals(),
        context_instance = RequestContext(request),
        )

