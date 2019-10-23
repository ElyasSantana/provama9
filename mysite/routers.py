from core.api.viewsets import ClienteViewSet, EnderecoViewSet
from rest_framework import routers as rt
from rest_framework_nested import routers as ntr

router = ntr.SimpleRouter()
router.register('cliente', ClienteViewSet, base_name='cliente')
router.register('endereco', EnderecoViewSet, base_name='endereco')
cliente_router = ntr.NestedSimpleRouter(router, 'cliente', lookup='cliente')
cliente_router.register('endereco', EnderecoViewSet, base_name='endereco')
"""
maildrops_router = routers.NestedSimpleRouter(client_router, r'maildrops', lookup='maildrop')
maildrops_router.register(r'recipients', MailRecipientViewSet, base_name='recipients')
for url in router.urls:
    print(url)
"""
for url in router.urls:
    print(url)