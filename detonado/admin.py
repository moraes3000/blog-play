from django.contrib import admin
from detonado.models.jogo import JogoModel
from detonado.models.capitulo_jogo import CapituloJogoModel
from detonado.models.estilo import EstiloDeJogoModel
from detonado.models.plataforma import PlataformaModel

admin.site.register(CapituloJogoModel)
admin.site.register(JogoModel)
admin.site.register(PlataformaModel)
admin.site.register(EstiloDeJogoModel)
