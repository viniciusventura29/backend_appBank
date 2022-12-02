from django.contrib import admin
from . import models

admin.site.register(models.Client)
admin.site.register(models.Conta)
admin.site.register(models.Endereco)
admin.site.register(models.Cartoes)