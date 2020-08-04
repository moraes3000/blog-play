from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.utils import unique_slug_generator


class PlataformaModel(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'plataforma'
        verbose_name_plural = 'plataforma em'

def plataforma_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(plataforma_pre_save_receiver, sender=PlataformaModel)
