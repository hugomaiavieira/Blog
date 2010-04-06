from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

class Artigo(models.Model):

    class Meta:
        ordering = ('-publicacao',)

    titulo = models.CharField(
        max_length=100,
        blank=False)
    conteudo = models.TextField(
        blank=False)
    publicacao = models.DateTimeField(
        default=datetime.now,
        blank=True)
    slug = models.SlugField(
        max_length=100,
        blank=True,
        unique=True)

    def get_absolute_url(self):
        return reverse('blog.views.artigo', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo


# SIGNALS

from django.db.models import signals
from utils.signals_comuns import slug_pre_save

signals.pre_save.connect(slug_pre_save, sender=Artigo)

