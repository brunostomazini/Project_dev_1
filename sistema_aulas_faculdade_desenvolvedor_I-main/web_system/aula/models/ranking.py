from .base_model import BaseModel
from django.db import models

class Ranking(BaseModel):
    rank = models.IntegerField( unique=True)
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0.0)
    nota = models.FloatField(default=0.0)
    regiao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.nome}'
