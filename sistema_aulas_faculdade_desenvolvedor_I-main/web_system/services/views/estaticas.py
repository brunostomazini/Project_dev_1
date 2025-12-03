from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from ..serialiazers import CalculoSerialiazer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'saudacao': reverse('services:saudacao', request=request, format=format),
        'saudacao_classe': reverse('services:saudacao_class', request=request, format=format),
        'calculo': reverse('services:calculo', request=request, format=format),
    })


@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao":"Olá Mundo!"})

class SaudacaoClass(APIView):
    def get(self, request):
        return Response({"saudacao":"Olá mundo em classe"})
    
@api_view(['GET','POST'])
def calculo(request):
    try:
        if request.method == 'GET':
            serialiazer = CalculoSerialiazer()
            return Response(serialiazer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            dados = JSONParser().parse(request)
            serialiazer = CalculoSerialiazer(data=dados)
            if serialiazer.is_valid():
                serialiazer.calculo()
                return Response(serialiazer.data, status=status.HTTP_200_OK)
            return JsonResponse(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        context = {
            'error':str(e)
        }
        return JsonResponse(context, status=status.HTTP_400_BAD_REQUEST, safe=False)

