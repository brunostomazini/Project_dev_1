from django.views import View
from aula.forms.perfil_form import PerfilForm
from aula.models import Perfil
from django.shortcuts import render, redirect, get_object_or_404

class PerfilListView(View):
    @staticmethod
    def get(request):
        perfils = Perfil.objects.all()
        context = {
            'perfils':perfils
        }
        return render(request, 'perfils/list.html', context)
    
class PerfilDetailView(View):
    @staticmethod
    def get(request, pk):
        perfil = Perfil.objects.get(id=pk)
        context = {
            'perfil' : perfil
        }

        return render(request, 'perfils/read.html', context)
