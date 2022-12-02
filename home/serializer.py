from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *
from pictures.contrib.rest_framework import PictureField
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }


    def validate(self, attrs):
        name_exists = Client.objects.filter(name=attrs["name"]).exists()
        cpf_exists = Client.objects.filter(cpf=attrs["cpf"]).exists()
        email_exists = Client.objects.filter(email=attrs["email"]).exists()

        if name_exists:
            raise ValidationError("Name has already been used")

        if cpf_exists:
            raise ValidationError("CPF has already been used")

        if email_exists:
            raise ValidationError("E-mail has already been used")

        return super().validate(attrs)


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