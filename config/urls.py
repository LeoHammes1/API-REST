from django.contrib import admin
from django.db import router
from django.urls import path, include
from Leitura.views import TelemetriaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Telemetria', TelemetriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
