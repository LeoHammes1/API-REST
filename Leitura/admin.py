from logging import addLevelName
from django.contrib import admin
from Leitura.models import Telemetria,Xid,NomeDoPonto

class Medidas(admin.ModelAdmin):
    list_display = ("xid","nomedoponto","dado","ts")
    list_display_links =("xid",)
    search_fields = ("xid","nomedoponto",)
    

class Nomedoponto(admin.ModelAdmin):
    list_display = ("nomedoponto",)
    list_display_links = ('nomedoponto',)
    search_fields = ("nomedoponto",)

class xid(admin.ModelAdmin):
    list_display = ("Xid",)
    list_display_links = ('Xid',)
    search_fields = ("Xid",)

admin.site.register(Telemetria,Medidas)
admin.site.register(Xid)
admin.site.register(NomeDoPonto)