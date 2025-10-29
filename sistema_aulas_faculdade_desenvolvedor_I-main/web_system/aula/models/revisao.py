from .base_model import BaseModel
from django.db import models

class Revisao(BaseModel):
    autor = models.CharField(max_length=100)
    '''nota deve ser int'''
    nota = models.FloatField(default=0.0)
    titulo = models.CharField(max_length=100)
    data_avaliacao = models.DateField()
    data_visita = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.nome}"
