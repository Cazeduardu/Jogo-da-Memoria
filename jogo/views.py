class JogoView(TemplateView):
    # O Django já olha dentro de 'templates' de cada app automaticamente
    template_name = 'tabuleiro.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        icones = ['🐍', '⭐', '🚀', '🔥', '💻', '🎮', '🍕', '🌈']
        # Criar pares e embaralhar
        import random
        cartas = icones * 2
        random.shuffle(cartas)
        context['cartas'] = cartas
        return context