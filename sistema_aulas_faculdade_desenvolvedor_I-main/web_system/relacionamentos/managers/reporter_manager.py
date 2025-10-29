from datetime import date
from django.db.models import QuerySet
from .base_manager import BaseManager

class ReporterManager(BaseManager):

    def find_by_nome(self, nome: str) -> list['Reporter']:
        if isinstance(nome, str) and len(nome) >0 :
            consulta = self.filter(name__icontains='name')
            return list(consulta)
        else:
            raise TypeError('O nome deve ser string e nao...')


    #def find_by_