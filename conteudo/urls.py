from django.urls import path
from conteudo.views import PaginaListView,PaginaDetalhe


urlpatterns = [
    path('', PaginaListView.as_view(),name='PaginaListView'),
    path('pagina/<slug:slug>/', PaginaDetalhe.as_view(), name='PaginaDetalhe-detail'),
]