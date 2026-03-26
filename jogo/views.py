from django.views.generic import TemplateView
import random

class JogoView(TemplateView):
    template_name = 'tabuleiro.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lista de ícones (emojis) para o jogo
        icones = ['🐍', '⭐', '🚀', '🔥', '💻', '🎮', '🍕', '🌈']
        
        # Criamos os pares, duplicando a lista e embaralhando
        cartas = icones * 2
        random.shuffle(cartas)
        
        context['cartas'] = cartas
        return context