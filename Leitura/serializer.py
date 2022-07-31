from dataclasses import fields
from rest_framework import serializers
from Leitura.models import Telemetria,Xid,NomeDoPonto


class XidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xid
        fields = ["Xid"]

class NomedopontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomeDoPonto
        fields = ["NomeDoPonto"]

class TelemetriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetria
        fields = ['xid', 'nomedoponto','dado', 'ts',"Ano","Trimestre","Mês","Dia","Ordem"]


