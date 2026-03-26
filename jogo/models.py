from django.db import models
from django.contrib.auth.models import User

class Partida(models.Model):
    jogador = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    tempo_segundos = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pontuacao', 'tempo_segundos']