from django.db import models
from django.utils.translation import gettext_lazy as _

class Genero(models.TextChoices):
    MALE = "MALE", _('Masculino')
    FEMALE = "FEMALE", _('Feminino')
    OUTRO = "OUTRO", _('Outro')
    NOT_SPECIFIED = "NOT_SPECIFIED", _('Não especificado')
