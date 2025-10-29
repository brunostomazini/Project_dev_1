from aula.forms.perfil_form import PerfilForm
from aula.models import Perfil
from django.shortcuts import render, redirect, get_object_or_404


def perfil_list(request):
    perfils = Perfil.objects.all()

    context = {
        'perfils': perfils
    }

    return render(request, 'perfils/list.html', context)

def perfil_detail(request, pk):
    perfil = Perfil.objects.get(id=pk)
    context = {
        'perfil' : perfil
    }

    return render(request, 'perfils/read.html', context)

def perfil_delete(request, perfil_id):
     perfil = get_object_or_404(Perfil, pk=perfil_id)

     try:
         if request.method == 'POST':
             v_perfil_id = request.POST.get('perfil_id', None)
             if int(v_perfil_id) == perfil_id:
                 perfil.delete()
                 return redirect('app:perfil_list')
         else:
             context = {
                 'perfil':perfil
             }
             return render(request, 'perfils/delete.html', context)
     except:
        context = {}
        return render(request, "perfils/list.html", context)
     
def perfil_create(request):
    if request.method =='POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:perfil_list')
        
    else:
        form = PerfilForm()

    context = {
        'form':form
    }
    return render(request, 'perfils/create_simple.html', context)

def perfil_update(request, perfil_id):
    perfil = get_object_or_404(Perfil, pk=perfil_id)
    if request.method =='POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('app:perfil_list')
        
    else:
        form = PerfilForm(instance=perfil)

    context = {
        'form':form,
        'perfil':perfil

    }

    return render(request, 'perfils/update.html', context)