from django.contrib import admin
from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Conta)
admin.site.register(models.Endereco)
admin.site.register(models.Cartoes)