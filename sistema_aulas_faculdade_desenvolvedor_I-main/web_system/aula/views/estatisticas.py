from datetime import datetime
from django.shortcuts import HttpResponse,render
from aula.models import Perfil

def primeira_view(request):
    contesto = {
        'mensagem':'Bom dia Dev',
    }
    return render(request, 'primeira.html', contesto )
    


def saudacao(request):
    agora = datetime.now()
    mensagem = "Boa noite"
    if 12 > agora.hour > 6:
        mensagem ="Bom dia"
    elif 0 < agora.hour <= 6:
        mensagem ="Boa Madrugada"


    completo ={
        'mensagem':mensagem,
        'horario':agora
    }
    return render(request, 'primeira.html', completo)

"""def nome(request, name):
    perfil - Perfil.objects.find_by_name(name)
    objeto = serializers.serialize('python', perfil)
    return  JsonResponse(object, safe=False)"""

def teste(request):
   pass

