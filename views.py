from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

from tags.models import Tag

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    assunto = forms.CharField(max_length=100,required=False)
    mensagem = forms.Field(widget=forms.Textarea, required=True)

    def enviar(self):
        titulo = "[Blog do Hugo] %(assunto)s" % self.cleaned_data
        origem = "contato@hugomaiavieira.com"
        destino = "hugouenf@gmail.com"
        texto = """
Nome: %(nome)s

E-mail: %(email)s

Mensagem:

%(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=origem,
            recipient_list=[destino],
            )

def contato(request):
    tags = Tag.objects.all().order_by("nome")

    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            aviso = 'Mensagem enviada com sucesso!'
    else:
        form = FormContato()


    return render_to_response(
        'contato.html',
        locals(),
        context_instance=RequestContext(request),
        )

