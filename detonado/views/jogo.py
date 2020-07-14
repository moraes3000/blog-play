from django.shortcuts import render
from django.views.generic import ListView, DetailView

from detonado.models.jogo import JogoModel
from detonado.models.capitulo_jogo import CapituloJogoModel

class JogoListView(ListView):
    model = JogoModel
    template_name = 'detonado/jogo/jogo-lista.html'
    # ordering = '-id'

