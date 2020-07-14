from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

class ColumaModel(models.Model):
    nome_coluna = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['nome_coluna']
        verbose_name = 'Coluna'
        verbose_name_plural = 'Colunas'

    def __str__(self):
        return self.nome_coluna

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome_coluna)


@receiver(pre_save, sender=ColumaModel)
def nome_slug(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
