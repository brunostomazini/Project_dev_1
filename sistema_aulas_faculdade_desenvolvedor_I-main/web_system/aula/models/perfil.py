from .base_model import BaseModel
from django.db import models
from aula.managers.perfil_manager import Perfil_Manager

from ..enumerations import Genero


class Perfil(BaseModel):
    cidade = models.CharField(default='', max_length=255, verbose_name='Cidade', help_text='Cidade onde mora atualmente.')
    pais = models.CharField(default='', max_length=60, verbose_name='País', help_text='País onde mora atualmente.')
    bio = models.TextField(default='', verbose_name='Biografia', help_text='Biografia do usuário.')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    passaporte = models.CharField(default='', max_length=10, verbose_name='Passaporte', help_text='Número do passaporte.')
    genero = models.CharField(max_length=20, choices=Genero, default=Genero.NOT_SPECIFIED, verbose_name='Gênero')

    # modelo mto melhor, mas n é oq o sor quer:
    # genero = models.TextChoices('Masculino', 'Feminino', 'Outro', verbose_name='Gênero', helpText='Gênero do usuário')

    def __str__(self):
        return f"Perfil ID - {self.id}"


    objects = Perfil_Manager