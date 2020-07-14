from django.urls import path
from detonado.views.jogo import JogoListView
from detonado.views.capitulo import CapituloJogoListView,CapituloDetail

urlpatterns = [
    path('lista-de-jogo', JogoListView.as_view(), name='JogoListView'),
    path('lista-de-jogo/<slug:slug>/', CapituloJogoListView.as_view(), name='CapituloJogoListView'),
    path('lista-de-jogo/<slug:jogo>/capitulo/<slug:slug>/', CapituloDetail.as_view(), name='CapituloDetail'),

]
