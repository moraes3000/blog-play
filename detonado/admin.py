from django.contrib import admin
from detonado.models.jogo import JogoModel
from detonado.models.capitulo_jogo import CapituloJogoModel
from detonado.models.estilo import EstiloDeJogoModel
from detonado.models.plataforma import PlataformaModel


class CapituloJogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'chave_estrangeira')


class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug')


admin.site.register(CapituloJogoModel, CapituloJogoAdmin)
admin.site.register(JogoModel,JogoAdmin)
admin.site.register(PlataformaModel)
admin.site.register(EstiloDeJogoModel)
