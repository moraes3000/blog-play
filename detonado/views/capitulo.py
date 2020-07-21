from django.shortcuts import render
from django.views.generic import ListView, DetailView

from detonado.models.capitulo_jogo import CapituloJogoModel
from detonado.models.jogo import JogoModel


class CapituloJogoListView(ListView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-listar.html"

    # ordering = '-id'

    def get_context_data(self, **kwargs):
        context = {}
        context = super().get_context_data()
        slug = self.kwargs.get('slug')
        context['titulo_header'] = "Gerais"
        context['capitulos'] = CapituloJogoModel.objects.filter(chave_estrangeira__slug=slug)
        return context


class CapituloJogoHistoriaListView(ListView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-listar.html"
    ordering = 'nome'

    def get_context_data(self, **kwargs):
        context = {}
        context = super().get_context_data()
        slug = self.kwargs.get('slug')
        context['titulo_header'] = "Modo História"
        context['capitulos'] = CapituloJogoModel.objects.filter(chave_estrangeira__slug=slug).filter(tipo_fase="H")
        return context


class CapituloJogoSecundariaListView(ListView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-listar.html"
    ordering = 'nome'

    def get_context_data(self, **kwargs):
        context = {}
        context = super().get_context_data()
        slug = self.kwargs.get('slug')
        context['titulo_header'] = "Secundárias"
        context['capitulos'] = CapituloJogoModel.objects.filter(chave_estrangeira__slug=slug).filter(tipo_fase="S")
        return context

class CapituloJogoConquistaListView(ListView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-listar.html"
    ordering = 'nome'

    def get_context_data(self, **kwargs):
        context = {}
        context = super().get_context_data()
        slug = self.kwargs.get('slug')
        context['titulo_header'] = "Conquista"
        context['capitulos'] = CapituloJogoModel.objects.filter(chave_estrangeira__slug=slug).filter(tipo_fase="C")
        return context


class CapituloDetail(DetailView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-detalhe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['plataformas'] = self.get_object().chave_estrangeira.plataforma_fk.all()
        context['estilos_jogos'] = self.get_object().chave_estrangeira.estitlo_de_jogo_fk.all()

        return context
