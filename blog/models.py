from django.db import models
from django.utils import timezone

class Jogador(models.Model):
    Nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    Data_de_Nascimento = models.DateField()
    Email = models.EmailField()
    Nacionalidade = models.CharField(max_length=15)
    Titulos = models.IntegerField()

    def __str__(self):
        return self.Nome

class Time(models.Model):
    Razão_Social = models.CharField(max_length=50)
    '''Mascote = models.ImageField(null=True)'''
    CNPJ = models.CharField(max_length=14)
    Email = models.EmailField()
    Jogadores = models.ManyToManyField('Jogador')
    def __str__(self):
        return self.Razão_Social
class Jogo(models.Model):
    Times = models.ManyToManyField('Time')
    Data = models.DateTimeField()
    Resultado = models.CharField(max_length=30)
    

