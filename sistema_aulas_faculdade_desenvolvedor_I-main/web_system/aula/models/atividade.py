from .base_model import BaseModel
from django.db import models
from django.contrib import admin

class Atividade(BaseModel):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=8,
                             null=True,
                             blank=True)
    nota = models.FloatField(default=0.0,)
    duracao = models.FloatField(default=0.0)
    ingresso = models.BooleanField(default=False)
    informacoes = models.TextField(default='')
    guia = models.BooleanField(default=False)
    endereco = models.CharField(max_length=100, default='')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('nome',)
    list_filter = ('updated_at',)