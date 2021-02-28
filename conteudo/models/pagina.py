from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from conteudo.models import TagModel

# Create your models here.
from core.utils import unique_slug_generator


class PaginaModel(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    conteudo = RichTextUploadingField(u'Conteúdo', default='', blank=True, null=True)
    tag_fk = models.ForeignKey(TagModel, verbose_name='Tags ', related_name='+', default='',
                               blank=True, null=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='pagina/thumbnail', null=True, blank=True)
    publicado_home = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.nome

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)


def pagina_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pagina_pre_save_receiver, sender=PaginaModel)
