from rest_framework import viewsets
from core.models import Cliente, Endereco
from core.api.serializers import ClienteSerializer, EnderecoSerializer
from rest_framework.decorators import action


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        cliente_id = self.request.query_params.get('id', None)
        queryset = Cliente.objects.all()

        if cliente_id:
            queryset = queryset.filter(id=cliente_id)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ClienteViewSet,
                     self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ClienteViewSet, self).destroy(request, *args, **kwargs)


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        #cliente_id = self.request.query_params.get('enderecos', None)
        queryset = Endereco.objects.all()

        return queryset

    def list(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(EnderecoViewSet,
                     self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(EnderecoViewSet, self).destroy(request, *args, **kwargs)
