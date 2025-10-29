from django.db.models import QuerySet
from .base_manager import BaseManager

def Perfil_Manager(BaseManager):

    def find_by_nome(self, name: str) -> QuerySet['Perfil']:
        if isinstance(name, str):
            consulta = self.filter(nome__icontains=name)
            return consulta
        else:
            raise TypeError('O nome deve ser uma string')