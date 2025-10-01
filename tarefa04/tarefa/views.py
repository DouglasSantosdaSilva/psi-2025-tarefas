from django.shortcuts import render
from .models import Tarefa
from datetime import date



def index(request):
    hoje = date.today()
    tarefas = Tarefa.objects.all()
    return render(request, 'index.html', {
        'tarefas': tarefas,
        'hoje': hoje
    })
