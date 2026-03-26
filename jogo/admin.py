from django.contrib import admin
from .models import Partida

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('jogador', 'pontuacao', 'tempo_segundos', 'data')