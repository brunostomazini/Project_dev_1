from aula.forms.perfil_form import PerfilForm
from aula.models import Perfil
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('aula.view_perfil', raise_exception=True)
@require_http_methods(['GET'])
def perfil_list(request):
    perfils = Perfil.objects.all()

    context = {
        'perfils': perfils
    }

    return render(request, 'perfils/list.html', context)


#@require_http_methods(['GET'])
def perfil_detail(request, pk):
    perfil = Perfil.objects.get(id=pk)
    context = {
        'perfil' : perfil
    }
    return render(request, 'perfils/read.html', context)


#@require_http_methods(['GET','POST'])
def perfil_delete(request, pk):
     perfil = get_object_or_404(Perfil, pk=pk)
     try:
         if request.method == 'POST':
             v_perfil_id = request.POST.get('perfil_id', None)
             if int(v_perfil_id) == pk:
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


#@require_http_methods(['GET','POST']) 
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

#@require_http_methods(['GET','POST'])
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