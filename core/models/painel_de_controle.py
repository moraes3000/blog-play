from django.db import models

# Create your models here.

class PainelDeControleModel(models.Model):
    logo = models.ImageField(upload_to='logo/', default=True, blank=True)
    css_editor = models.TextField(blank=True, null=True)
    js_editor = models.TextField(blank=True, null=True)
    font_editor = models.TextField(blank=True, null=True)

