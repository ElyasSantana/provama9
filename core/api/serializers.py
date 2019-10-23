from rest_framework import serializers
from core.models import Cliente, Endereco


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
