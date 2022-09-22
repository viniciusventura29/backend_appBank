from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cliente
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Endereco
        fields = '__all__'

class ContatosSerializer(serializers.ModelSerializer):
    class Meta :
        model = Contatos
        fields = '__all__'

class ContaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Conta
        fields = '__all__'

class CartoesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cartoes
        fields = '__all__'

class FaturaSerielizer(serializers.ModelSerializer):
    class Meta:
        model: Fatura
        field = '__all__'

class TransacoesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Transacoes
        fields = '__all__'

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Extrato
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Emprestimo
        fields = '__all__'

class Pgmt_emprestimoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Pgmt_emprestimo
        fields = '__all__'

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta :
        model = Favoritos
        fields = '__all__'