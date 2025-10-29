from django.contrib import admin

from aula.models import Atividade, AtividadeAdmin
from aula.models import Perfil
from aula.models import Lugar
from aula.models import Pergunta
from aula.models import Ranking
from aula.models import Revisao
from aula.models import Viagem



# Register your models here.

admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Perfil)
admin.site.register(Lugar)
admin.site.register(Pergunta)
admin.site.register(Ranking)
admin.site.register(Revisao)
admin.site.register(Viagem)
