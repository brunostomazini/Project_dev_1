from datetime import datetime
from django.shortcuts import HttpResponse, render
from django.views import View


class saudacaoView(View):
    @staticmethod
    def get( request):
        agora = datetime.now()
        mensagem = "bom noite!"
        if 12 > agora.hour >6:
            mensagem = "bom dia!"

        elif 0 < agora.hour <=6:
            mensagem = "boa madrugada!"


        completo = {
            'mensagem':mensagem
        }

        return render(request, 'primeira.html', completo)