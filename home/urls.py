from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()

router.register('Cliente',ClienteListView)
router.register('Endereco',EnderecoListView)
router.register('Contatos',ContaListView)
router.register('Conta',ContaListView)
router.register('Cartoes',CartoesListView)
router.register('Fatura',FaturaListView)
router.register('Transacoes',TransacoesListView)
router.register('Extrato',ExtratoListView)
router.register('Emprestimo',EmprestimoListView)
router.register('Pgmt_emprestimo',Pgmt_emprestimoListView)
router.register('Favoritos',FavoritosListView)



urlpatterns = router.urls