from django.views import View
from aula.forms.perfil_form import PerfilForm
from aula.models import Perfil
from django.shortcuts import render, redirect, get_object_or_404
import random
import string
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

class PerfilListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url=reverse_lazy('login')
    permission_required='aula.view_perfil'

    @staticmethod
    def get(request):
        perfils = Perfil.objects.all()
        context = {
            'perfils':perfils
        }
        return render(request, 'perfils/list.html', context)
    
class PerfilDetailView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url=reverse_lazy('login')
    permission_required='aula.view_perfil'

    @staticmethod
    def get(request, pk):
        perfil = Perfil.objects.get(id=pk)
        context = {
            'perfil' : perfil
        }

        return render(request, 'perfils/read.html', context)

class CodeGenerate(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('login')
    permission_required = 'aula.generate_code_perfil'

    @staticmethod
    def get(request, pk):
        novoCodigo = get_object_or_404(Perfil, pk=pk)
        try:
            letters = string.ascii_letters + string.digits
            novoCodigo.cidade = "".join(random.choice(letters) for i in range(10))
            novoCodigo.save()
            return redirect('aula:perfil_class_list')
        except:
            print(f"")
            return redirect('aula:perfil_class_list')
        
class PerfilDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url=reverse_lazy('login')
    permission_required='aula.delete_perfil'

    
    '''def get(self, request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        return render(request, 'perfils/delete.html', {'perfil': perfil})

    def post(self, request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        perfil.delete()
        messages.success(request, 'Perfil deletado com sucesso!')
        return redirect('aula:perfil_list')'''

    @staticmethod
    def get(request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        try:
            context = {
                'perfil':perfil
            }
            return render(request, 'perfils/delete.html', context)
        except Exception as e:
            context ={}
            print(e)
            return render(request, 'perfils/list.html', context)
        
    @staticmethod
    def post(request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        try:
            v_perfil_id = request.POST.get("perfil_id", None)
            if int(v_perfil_id) == pk:
                perfil.delete()
                context = {
                    'message':"Deleção concluida com sucesso"
                }
                #return render(request, 'perfils/list.html', context)
                return redirect('app:perfil_list')
        except Exception as e:
            print(f"Erro ao deletar perfil: {e}")
            context = {'error': 'Não foi possível deletar o perfil.'}
            return render(request, 'perfils/list.html', context)
    

class PerfilCreate(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url=reverse_lazy('login')
    permission_required='aula.add_perfil'

    @staticmethod
    def get(request):
        form = PerfilForm()
        context = {
            'form':form
        }
        return render(request, 'perfils/create_simple.html', context)
    
    @staticmethod
    def post(request):
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aula:perfil_class_list')
        context = {
            'form': form
        }
        return render(request, 'perfils/create_simple.html', context)
    
class PerfilUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('login')
    permission_required = 'aula.change_perfil'

    def get(self, request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        form = PerfilForm(instance=perfil)  # Pass the object to the form for editing
        context = {'form': form, 'perfil': perfil}
        return render(request, 'perfils/update.html', context)

    def post(self, request, pk):
        perfil = get_object_or_404(Perfil, pk=pk)
        form = PerfilForm(request.POST, instance=perfil)
        
        if form.is_valid():
            form.save()  # Save the updated object
            return redirect('perfils:list')  # Redirect to list page after successful update
        else:
            context = {'form': form, 'perfil': perfil}
            return render(request, 'perfils/update.html', context)