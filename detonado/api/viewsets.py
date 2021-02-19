from rest_framework.viewsets import ModelViewSet
from detonado.api.serializers import JogoSerializer
from detonado.models.jogo import JogoModel


class JogoViewSetViewSet(ModelViewSet):
    queryset = JogoModel.objects.all()
    serializer_class = JogoSerializer
