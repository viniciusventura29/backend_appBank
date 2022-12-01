from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

class CutomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer
    def post(self, request, *args, **kwargs):
        print("-"*50)
        
        return super().post(request, *args, **kwargs)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        client_data = request.data 

        new_client = Client.objects.create_superuser(
            email=client_data["email"],
            password=client_data["password"],
            cpf=client_data["cpf"],
        )

        serializer = ClientSerializer(new_client)

        return Response(serializer.data)

class ClienteListView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteInsertImageListView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteInsertImageSerializer

class EnderecoListView(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContatosListView(viewsets.ModelViewSet):
    queryset = Contatos.objects.all()
    serializer_class = ContatosSerializer

class ContaListView(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartoesListView(viewsets.ModelViewSet):
    queryset = Cartoes.objects.all()
    serializer_class = CartoesSerializer

class FaturaListView(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerielizer

class TransacoesListView(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer

class ExtratoListView(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

class EmprestimoListView(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class Pgmt_emprestimoListView(viewsets.ModelViewSet):
    queryset = Pgmt_emprestimo.objects.all()
    serializer_class = Pgmt_emprestimoSerializer

class FavoritosListView(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritosSerializer