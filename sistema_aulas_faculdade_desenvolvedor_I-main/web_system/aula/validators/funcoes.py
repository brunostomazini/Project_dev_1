from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validator_par(valor):
    try:
        if int(valor) % 2 !=0:
            raise ValidationError(
                _("não é um valor par"),
                params={'valor': valor},
            )
    except ValueError:
        pass