from django.db import models


class Estado (models.Model):
    nome = models.CharField(max_length=255)
    populacao = models.IntegerField()
    idade = models.IntegerField()
    sigla = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'estado'
        app_label = 'app'

        
class Cidade (models.Model):
    nome = models.CharField(max_length=255)
    populacao = models.IntegerField()
    idade = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cidade'
        app_label = 'app'
        

class ClimaCidade (models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'clima'
        app_label = 'app'