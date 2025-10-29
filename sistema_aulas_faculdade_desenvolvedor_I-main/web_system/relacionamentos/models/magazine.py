from django.db import models
from .base_model import BaseModel

class Magazine(BaseModel):
    nome = models.CharField(max_length=100)
    edicao = models.CharField(max_length=100)
