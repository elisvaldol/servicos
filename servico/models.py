from django.db import models
from django.conf import settings
from django.utils import timezone




class cliente(models.Model):
    CPf = models.CharField(max_length=14)
    Nome = models.CharField(max_length=100)
    Endereço = models.CharField(max_length=100)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Telefone1 = models.CharField(max_length=10)
    Telefone2 = models.CharField(max_length=10)


class servicos(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Descricao = models.CharField(max_length=100)
    Valor = models.FloatField(blank=True, null=True)
    Obs = models.TextField(max_length=200)
    Data_criacao = models.DateTimeField(default=timezone.now)
    Data_execucao = models.DateTimeField(blank=True, null=True)

    def cadastramento(self):
        self.cadastramento_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Descricao



# Create your models here.
