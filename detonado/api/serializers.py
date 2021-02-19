from rest_framework.serializers import ModelSerializer

from detonado.models.jogo import JogoModel


class JogoSerializer(ModelSerializer):
    class Meta:
        model = JogoModel
        fields = ('id','nome', 'descricao')
