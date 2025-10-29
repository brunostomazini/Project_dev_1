from .base_model import BaseModel
from django.db import models

class Lugar(BaseModel):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    ingresso = models.BooleanField(default=False)
    horario_funcinamento = models.CharField(verbose_name = "Horário de Funcionamento",
                             max_length=8,
                             null=True,
                             blank=True)
    horario_fechamento = models.CharField(verbose_name = "Horário de Fechamento",
                                          max_length=8)
    nota = models.FloatField(default=0.0)
    acessibiliade = models.BooleanField(verbose_name="Acessibilidade", default=False)
    classificacao = models.BooleanField(verbose_name="Classificacao", default=False)
    contato = models.EmailField(verbose_name="Email para Contato")

    def __str__(self):
        return f"{self.id} - {self.nome}"
