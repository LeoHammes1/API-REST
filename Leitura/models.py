from django.db import models
from django.forms import CharField

        
class Telemetria(models.Model):
    
    xid = models.CharField(max_length=20)
    nomedoponto = models.CharField(max_length=30)
    ts = models.DateTimeField()
    dado = models.CharField(max_length=30)
    Ano = models.CharField(max_length=4)
    Trimestre = models.CharField(max_length=2)
    Mês = models.CharField(max_length=2)
    Dia = models.CharField(max_length=2)
    Ordem = models.CharField(max_length=1)

    def __str__(self):
        return str(self.xid)
