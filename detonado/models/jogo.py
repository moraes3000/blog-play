from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.utils import unique_slug_generator
from conteudo.models import TagModel
from detonado.models.plataforma import PlataformaModel
from detonado.models.estilo import EstiloDeJogoModel

# otimizar o tamanho da imagem
from PIL import Image
from django.conf import settings
import os
from image_cropping import ImageCropField, ImageRatioField

class JogoModel(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)
    descricao = RichTextField(default='', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='jogo/thumb', default=True, blank=True)
    cropping = ImageRatioField('thumbnail', '250x350')
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

    #reduzir o tamanho

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.resize_image(self.thumbnail.name, 300)
    #
    # @staticmethod
    # def resize_image(img_name, new_width):
    #     img_path = os.path.join(settings.MEDIA_ROOT, img_name)
    #     img = Image.open(img_path)
    #     width, height = img.size
    #     new_height = round((new_width * height) / width)
    #
    #     if width <= new_width:
    #         img.close()
    #         return
    #
    #     new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    #     new_img.save(
    #         img_path,
    #         optimize=True,
    #         quality=60
    #     )
    #     new_img.close()

    def __str__(self):
        return self.nome

    # def get_absolute_url(self):
    #     return reverse('viewlistagem')

def product_pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=JogoModel)


# @receiver(pre_save, sender=JogoModel)
# def slug_automatico(sender, instance, **kwargs):
#     instance.slug = instance.generate_slug()
