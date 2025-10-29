from django.views import View
from aula.forms.perfil_form import PerfilForm
from aula.models import Perfil
from django.shortcuts import render, redirect, get_object_or_404
import random
import string

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

class CodeGenerate(View):

    @staticmethod
    def get(request, pk):
        novoCodigo = get_object_or_404(Perfil, pk=pk)
        try:
            letters = string.ascii_letters + string.digits
            novoCodigo.cidade = "".join(random.choice(letters) for i in range(10))
            novoCodigo.save()
            return redirect('aula:Perfil_class_list')
        except:
            print(f"")
            return redirect('aula:Perfil_class_list')
        
class PerfilDeleteView(View):

    @staticmethod
    def get(request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        try:
            context = {
                'perfil':perfil
            }
            return render(request, 'perfil/delete.html', context)
        except Exception as e:
            context ={}
            print(e)
            return render(request, 'perfil/list.html', context)
        
    """@staticmethod
    def post(request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        try:
            v_perfil_id = request.POST.get("perfil_id", None)
            if int(v_perfil_id) == pk:
                perfil.delete()
                return render(request, 'perfil/list.html', context)
        except Exception as e:
            context ={}
            print(e)
            return render(request, 'perfil/list.html', context)"""
    

class PerfilCreate(View):

    @staticmethod
    def get(request):
        form = PerfilForm
        context = {
            'form':form
        }
        return render(request, 'perfils/create_simple.html', context)
    
    @staticmethod
    def post(request):
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aula:Perfil_class_list')
        context = {
            'form': form
        }
        return render(request, 'perfils/create_simple.html', context)