from django.urls import path
from detonado.views.jogo import JogoListView, JogoListPlataformaView, JogoListEstiloView
from detonado.views.capitulo import CapituloJogoListView,CapituloDetail
from detonado.views.plataforma import PlataformaView

urlpatterns = [
    path('lista-de-jogo', JogoListView.as_view(), name='JogoListView'),
    path('lista-de-jogo/<slug:slug>/', CapituloJogoListView.as_view(), name='CapituloJogoListView'),
    path('lista-de-jogo/<slug:jogo>/capitulo/<slug:slug>/', CapituloDetail.as_view(), name='CapituloDetail'),

    path('plataforma/<slug:slug>/', JogoListPlataformaView.as_view(), name='JogoListPlataformaView'),
    path('estilo/<slug:slug>/', JogoListEstiloView.as_view(), name='JogoListEstiloView'),



]
