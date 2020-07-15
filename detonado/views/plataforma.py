from django.shortcuts import render
from django.views.generic import ListView, DetailView

from detonado.models.jogo import JogoModel
from detonado.models.plataforma import PlataformaModel

class PlataformaView(ListView):
    model = PlataformaModel
    template_name = 'detonado/plataforma/plataforma-listar.html'
    # ordering = '-id'

