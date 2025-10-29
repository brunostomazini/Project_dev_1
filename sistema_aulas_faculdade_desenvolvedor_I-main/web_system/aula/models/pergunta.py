from .base_model import BaseModel
from django.db import models

class Pergunta(BaseModel):
    nome = models.CharField(max_length=100)
