from rest_framework.viewsets import ModelViewSet

from conteudo.api.serializers import TagSerializer, PaginaSerializer
from conteudo.models import TagModel, PaginaModel


class TagViewSetViewSet(ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer


class PaginaViewSetViewSet(ModelViewSet):
    queryset = PaginaModel.objects.all()
    serializer_class = PaginaSerializer
    lookup_field = 'slug'
