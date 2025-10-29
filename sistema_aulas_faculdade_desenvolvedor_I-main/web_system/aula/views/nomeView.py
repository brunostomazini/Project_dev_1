from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect
from django.views import View
from django.core import serializers
from pyexpat.errors import messages

from ..models import Perfil

class NomeView(View):
    @staticmethod
    def get(request,cidade):


        pessoas = list(Perfil.objects.all())

        tipo =str(request.GET.get("type"))
        match tipo.lower():
            case "http":

                mensagem = ""
                for objecst in pessoas:
                    mensagem += f"<p>Cidade:{objecst.cidade}<br></p><p>Pais:{objecst.pais}<br></p><hr>"

                return HttpResponse(mensagem,status=200)

            case "json":
                objeto = serializers.serialize('python', pessoas)
                return JsonResponse(objeto, safe=False)


            case _:
                return redirect('https://http.dog/400.jpg')



