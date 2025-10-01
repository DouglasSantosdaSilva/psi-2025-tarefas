from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    prazo = models.DateField()
    
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.nome