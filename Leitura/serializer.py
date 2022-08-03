from dataclasses import fields
from rest_framework import serializers
from Leitura.models import Telemetria


class TelemetriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetria
        fields = ['xid', 'nomedoponto','dado', 'ts',"Ano","Trimestre","Mês","Dia","Ordem"]


