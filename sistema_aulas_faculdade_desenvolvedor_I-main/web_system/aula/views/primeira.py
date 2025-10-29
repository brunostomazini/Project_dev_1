from django.shortcuts import HttpResponse,render
from django.views import View

class PrimeiraView(View):
    @staticmethod
    def get(request):
        mensagem = {'mensagem':request.META['REMOTE_ADDR']}
        return render(request, 'primeira.html', mensagem)