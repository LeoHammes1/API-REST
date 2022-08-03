from argparse import Action
import codecs
from dataclasses import field, fields
from distutils.command.upload import upload
from itertools import product
from django.forms import DateTimeField
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from Leitura import serializer
from Leitura.admin import Nomedoponto

from Leitura.models import Telemetria
from Leitura.serializer import TelemetriaSerializer

fs = FileSystemStorage(location='temp/')

class TelemetriaViewSet(viewsets.ModelViewSet):
    queryset = Telemetria.objects.all()
    serializer_class = TelemetriaSerializer

    @action(detail=False,methods=['POST'])

    def upload_data(self,request):
        file = request.FILES.get("file")

        reader = csv.DictReader(codecs.iterdecode(file,"utf-8"),delimiter=",")

        data = list(reader)

        serializer = self.serializer_class(data=data, many =True)
        serializer.is_valid(raise_exception=True)

        telemetria_list = []
        for row in serializer.data:
            telemetria_list.append(
                Telemetria(
                    
                    xid = row ["xid"],
                    nomedoponto = row ["nomedoponto"],
                    ts = row["ts"],
                    dado = row["dado"],
                    Ano = row["Ano"],
                    Trimestre = row["Trimestre"],
                    Mês = row["Mês"],
                    Dia = row["Dia"],
                    Ordem = row["Ordem"],
                )
            )
        Telemetria.objects.bulk_create(telemetria_list)

        return Response("Importado")
