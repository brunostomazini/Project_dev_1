from django.db.models import QuerySet
from .base_manager import BaseManager

class PersonManager(BaseManager):

    def find_by_nome(self, name: str) -> QuerySet['Person']:
        if isinstance(name, str):
            consulta = self.filter(nome__icontains=name)
            return consulta
        else:
            raise TypeError('O nome deve ser uma string')