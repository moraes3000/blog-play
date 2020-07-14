from django.shortcuts import render
from django.views.generic import ListView, DetailView

from detonado.models.capitulo_jogo import CapituloJogoModel
from detonado.models.jogo import JogoModel

class CapituloJogoListView(ListView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-listar.html"

    # ordering = '-id'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        capitulos = CapituloJogoModel.objects.filter(chave_estrangeira__slug=slug)
        return capitulos



class CapituloDetail(DetailView):
    model = CapituloJogoModel
    template_name = "detonado/capitulo/capitulo-detalhe.html"

    def get_context_data(self, **kwargs):
        context =super().get_context_data()
        context['plataformas'] = self.get_object().chave_estrangeira.plataforma_fk.all()
        context['estilos_jogos'] = self.get_object().chave_estrangeira.estitlo_de_jogo_fk.all()

        return context


