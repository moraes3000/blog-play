from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class PlataformaModel(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Jogado em'
        verbose_name_plural = 'jogado em'

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)


@receiver(pre_save, sender=PlataformaModel)
def slug_automatico(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
