from django.contrib import admin
from .models.coluna import ColumaModel
from .models.template import TemplateModel
from .models.painel_de_controle import PainelDeControleModel

admin.site.register(ColumaModel)
admin.site.register(TemplateModel)
admin.site.register(PainelDeControleModel)

# Register your models here.
