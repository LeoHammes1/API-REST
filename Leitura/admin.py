from logging import addLevelName
from django.contrib import admin
from Leitura.models import Telemetria

class telemetria(admin.ModelAdmin):
    list_display = ("xid","nomedoponto","dado","ts")
    list_display_links =("xid",)
    search_fields = ("xid","nomedoponto",)
    
admin.site.register(Telemetria,telemetria)
