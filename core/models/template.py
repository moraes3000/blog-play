from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.models.coluna import ColumaModel


class TemplateModel(models.Model):
    nome_template = models.CharField(max_length=255)
    coluna_esquerda = models.ForeignKey(ColumaModel, verbose_name='Coluna Esquerda', related_name='+', default='',
                                        blank=True, null=True, on_delete=models.CASCADE)
    coluna_direita = models.ForeignKey(ColumaModel, verbose_name='Coluna Direita', related_name='+', default='',
                                       blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['nome_template']
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __str__(self):
        return self.nome_template

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome_template)


@receiver(pre_save, sender=TemplateModel)
def nome_slug(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
