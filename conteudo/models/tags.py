from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class TagModel(models.Model):
    nome_tag = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['nome_tag']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nome_tag

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome_tag)


@receiver(pre_save, sender=TagModel)
def nome_slug(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()