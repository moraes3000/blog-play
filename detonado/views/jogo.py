from django.shortcuts import render
from django.views.generic import ListView, DetailView

from detonado.models.jogo import JogoModel
from detonado.models.capitulo_jogo import CapituloJogoModel

class JogoListView(ListView):
    model = JogoModel
    template_name = 'detonado/jogo/jogo-lista.html'
    # ordering = '-id'


class JogoListPlataformaView(ListView):
    model = JogoModel
    template_name = 'detonado/plataforma/plataforma-listar.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        plataforma = JogoModel.objects.filter(plataforma_fk__slug=slug)
        return plataforma


class JogoListEstiloView(ListView):
    model = JogoModel
    template_name = 'detonado/estilo-de-jogo/estilo-listar.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        estilos = JogoModel.objects.filter(estitlo_de_jogo_fk__slug=slug)
        return estilos