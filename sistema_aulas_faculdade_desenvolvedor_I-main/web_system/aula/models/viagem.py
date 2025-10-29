from .base_model import BaseModel
from django.db import models

class Viagem(BaseModel):
    nome = models.CharField(max_length=50)
    transporte = models.TextChoices('Carro', 'Avião', 'Navio', 'Ônibus', 'Moto')