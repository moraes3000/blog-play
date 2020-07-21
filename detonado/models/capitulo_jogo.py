from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from detonado.models.jogo import JogoModel

class CapituloJogoModel(models.Model):
    MODO_CHOICES = (
        ("H", "História"),
        ("S", "Secundária"),
        ("C", "Conquista")
    )



    nome = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)
    descricao = RichTextUploadingField(u'Conteúdo', default='', blank=True, null=True)
    imagem = models.ImageField(upload_to="jogo/capitulo", default='', blank=True, null=True)
    criado = models.DateTimeField(default=timezone.now)
    chave_estrangeira = models.ForeignKey(JogoModel, verbose_name='Jogo ', related_name='+', default='',
                               blank=True, null=True, on_delete=models.CASCADE)
    tipo_fase = models.CharField(max_length=1, choices=MODO_CHOICES, default='H')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Capítulo do jogo'
        verbose_name_plural = 'Capítulos dos jogos'

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


@receiver(pre_save, sender=CapituloJogoModel)
def slug_automatico(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
