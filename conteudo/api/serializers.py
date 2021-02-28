from rest_framework.serializers import ModelSerializer

from conteudo.models import TagModel, PaginaModel


class TagSerializer(ModelSerializer):
    class Meta:
        model = TagModel
        fields = ('id', 'nome_tag', 'slug')


class PaginaSerializer(ModelSerializer):
    class Meta:
        model = PaginaModel

        fields = ('id', 'nome', 'slug', 'conteudo', 'tag_fk', 'thumbnail', 'publicado_home', 'url')

        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
