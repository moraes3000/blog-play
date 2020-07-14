from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from conteudo.models import TagModel


# Create your models here.
class PaginaModel(models.Model):
    nome_pagina = models.CharField(max_length=255)
    conteudo = RichTextUploadingField(u'Conteúdo', default='', blank=True, null=True)
    tag_fk = models.ForeignKey(TagModel, verbose_name='Tags ', related_name='+', default='',
                                       blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['nome_pagina']
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.nome_pagina

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome_pagina)


@receiver(pre_save, sender=PaginaModel)
def nome_slug(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()