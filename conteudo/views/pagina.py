from django.shortcuts import render
from django.views.generic import ListView, DetailView

from conteudo.models import PaginaModel

class PaginaListView(ListView):
    model = PaginaModel
    template_name = 'conteudo/pagina/pagina-listar.html'
    # ordering = '-id'


class PaginaDetalhe(DetailView):
    model = PaginaModel
    template_name = 'conteudo/pagina/pagina-detalhe.html'

