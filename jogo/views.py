from django.views.generic import ListView, TemplateView
from .models import Partida

class JogoView(TemplateView):
    template_name = 'jogo/tabuleiro.html'

class RankingView(ListView):
    model = Partida
    template_name = 'jogo/ranking.html'
    context_object_name = 'rankings'
    paginate_by = 10  # Ponto extra: Paginação