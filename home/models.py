from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from pictures.models import PictureField
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class Client(AbstractUser):
    username = None
    cpf = models.CharField(max_length=14, unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["email", "password"]

    def __str__(self):
        return self.name

class Cliente(models.Model):
    GEN_MASC = 'M'
    GEN_FEM = 'F'
    GEN_OUTROS = 'O'
    GEN_NAOESPECIFICADO = 'N'

    GENEROS = [
        (GEN_MASC, 'Genero masculino'),
        (GEN_FEM , 'Genero feminino'),
        (GEN_OUTROS , 'Genero outro'), 
        (GEN_NAOESPECIFICADO, 'Genero não especificado'),
    ]
    cpf = models.CharField(max_length=14, primary_key = True,null = False, blank = False)
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=30)
    nasc = models.DateField(null = False, blank = False)
    genero = models.CharField(max_length=1,choices=GENEROS,default=0)
    foto = PictureField(upload_to='loja/imagens/')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Endereco(models.Model):
    cpf = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cep = models.CharField(max_length=8,null = False, blank = False)
    rua = models.CharField(max_length=50,null = False, blank = False)
    bairro = models.CharField(max_length=50,null = False, blank = False)
    cidade = models.CharField(max_length=20,null = False, blank = False)
    estado = models.CharField(max_length=15,null = False, blank = False)
    numero = models.CharField(max_length=4,null = False, blank = False)
    complemento = models.CharField(max_length=10)
    
class Usuario(models.Model):
    cpf = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    senha = models.CharField(max_length=30,null = False, blank = False)

class Contatos(models.Model):
    cpf = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    celular = models.CharField(max_length=11)
    email = models.EmailField()

class Conta(models.Model):
    TIPO_POUPANCA = 'P'
    TIPO_CORRENTE = 'C'
    TIPO_SALARIO = 'S'

    TIPO_CONTA = [
        (TIPO_POUPANCA, 'Conta Poupança'),
        (TIPO_CORRENTE, 'Conta Corrente'),
        (TIPO_SALARIO, 'Conta Salário'),
    ]

    tipo_conta = models.CharField(max_length=1,choices=TIPO_CONTA,default=TIPO_CORRENTE)
    cpf = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

class Cartoes(models.Model):
    TIPO_STANDARD = 'S'
    TIPO_GOLD = 'G'
    TIPO_PLATINUM = 'P'
    TIPO_BLACK = 'B'

    TIPO_CARTAO = [
        (TIPO_STANDARD, 'Cartão Padrão'),
        (TIPO_GOLD, 'Cartão Gold'),
        (TIPO_PLATINUM, 'Cartão Platinum'),
        (TIPO_BLACK, 'Cartão Black'),
    ]

    conta = models.ForeignKey(Conta,on_delete=models.PROTECT)
    tipo_cartao = models.CharField(max_length=1, choices=TIPO_CARTAO, default=TIPO_STANDARD)
    numero = models.CharField(max_length=16, primary_key=True)
    bandeira = models.CharField(max_length=10)
    limite = models.DecimalField(max_digits=8,decimal_places=2)
    cvc = models.CharField(max_length=3)
    validade = models.DateField()
    dia_vencimento = models.IntegerField()

class Fatura(models.Model):
    cartao = models.ForeignKey(Cartoes,on_delete=models.PROTECT)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Transacoes(models.Model):
    conta_sender = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_sender')
    conta_reciver = models.ForeignKey(Conta, on_delete=models.PROTECT, related_name='conta_reciver')
    data = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Extrato(models.Model):
    transacao = models.ForeignKey(Transacoes, on_delete=models.PROTECT, null=True)
    conta = models.ForeignKey(Conta,on_delete = models.PROTECT)
    data = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=20)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

class Emprestimo(models.Model):
    conta = models.ForeignKey(Conta,on_delete = models.PROTECT)
    data_fisrt_parcela = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_parcelas = models.IntegerField()
    juros = models.DecimalField(max_digits=3,decimal_places=2)
    situacao = models.BooleanField()
    aprovado = models.BooleanField()

class Pgmt_emprestimo(models.Model):
    emprestimo = models.ForeignKey(Emprestimo,on_delete=models.PROTECT)
    data_vencimento = models.DateField()
    data_pag = models.DateField()

class Favoritos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    contato = models.ForeignKey(Contatos, on_delete=models.PROTECT)
    