from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from conteudo.models import TagModel
from detonado.models.plataforma import PlataformaModel
from detonado.models.estilo import EstiloDeJogoModel


class JogoModel(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    descricao = RichTextField(default='', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='jogo/thumb', default=True, blank=True)
    tag_fk = models.ForeignKey(TagModel, verbose_name='Tags ', related_name='+', default='',
                               blank=True, null=True, on_delete=models.CASCADE)

    criado = models.DateTimeField(default=timezone.now)
    desenvolvido = models.CharField(max_length=255, blank=True, null=True)
    ano_lancamento = models.CharField(max_length=250, blank=True, null=True)
    plataforma_fk = models.ManyToManyField('PlataformaModel', verbose_name="Plataforma do jogo", blank=True, null=True)
    estitlo_de_jogo_fk = models.ManyToManyField('EstiloDeJogoModel', verbose_name="Estilo De Jogo", blank=True,
                                                null=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def publish(self):
        self.criado = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    # def get_absolute_url(self):
    #     return reverse('viewlistagem')

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)


@receiver(pre_save, sender=JogoModel)
def slug_automatico(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
