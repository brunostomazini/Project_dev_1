from web_system.aula.models import baseModel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


@desconstructible
class CodeValidator:

    def __init__(self, cod="00000000"):
        self.code = cod

    def __call__(self, valor):
        if valor == self.code:
            raise ValidationError(
                _("Valor invalido"),
                params={"valor": valor},
            )

    def __eq__(self, other):
        return (
                isinstance(other, CodeValidator),
                self.code == other.code
        )