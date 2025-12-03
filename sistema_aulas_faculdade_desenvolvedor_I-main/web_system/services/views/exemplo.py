from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from aula.models import Perfil
from services.serialiazers import PerfilMinimalSerializer




class ExemploListService(APIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilMinimalSerializer

    def get(self, request, format=None):
        exemplo = Perfil.objects.all()
        context = {
            'request': request,
            'format': format
        }
        serializer = PerfilMinimalSerializer(exemplo, many=True,context=context)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        dados = request.data
        context = {
            'request': request,
            'format': format
        }
        serializer = PerfilMinimalSerializer(data=dados, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
