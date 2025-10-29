from .base_form import BaseForm
from aula.models.perfil import Perfil

class PerfilForm(BaseForm):
    class Meta:
        model = Perfil
        fields = '__all__'

