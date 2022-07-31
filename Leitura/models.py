from django.db import models

class Xid(models.Model):

    XID_CHOICES = (
        ("ID0001_TEMP", ("ID0001_TEMP")),
        ("ID0002_TEMP", ("ID0002_TEMP")),
        ("ID0003_TEMP", ("ID0003_TEMP")),
    )

    xid = models.CharField(max_length=20, choices=XID_CHOICES, blank=False,null=False)

    def __str__(self):
        return self.xid

class NomeDoPonto(models.Model):

    NOMEDOPONTO_CHOICES = (
        ("[Ambiente] Armazém 03",("[Ambiente] Armazém 03")),
        ("[Refrigerador] Divisão",("[Refrigerador] Divisão")),
        ("[Umidade 01] Sala Heparina",("[Umidade 01] Sala Heparina")),
    )

    nomedoponto = models.CharField(max_length=40,choices=NOMEDOPONTO_CHOICES,blank=True,null=False)

    def __str__(self):
        return self.nomedoponto

        
class Telemetria(models.Model):
    
    xid = models.ForeignKey(Xid, on_delete= models.CASCADE,related_name="Xid",null=True)  
    nomedoponto = models.ForeignKey(NomeDoPonto, on_delete= models.CASCADE, related_name="NomeDoPonto",null=True)
    ts = models.DateTimeField()
    dado = models.CharField(max_length=30)
    Ano = models.CharField(max_length=4)
    Trimestre = models.CharField(max_length=2)
    Mês = models.CharField(max_length=2)
    Dia = models.CharField(max_length=2)
    Ordem = models.CharField(max_length=1)

    def __str__(self):
        return str(self.xid)
