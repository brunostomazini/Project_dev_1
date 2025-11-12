from operator import index
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
import aula.views.estatisticas as views_funcoes
from aula.views import PrimeiraView
from aula.views import NomeView
from aula.views.perfil_classes import PerfilListView, PerfilDetailView, CodeGenerate, PerfilDeleteView, PerfilCreate
from aula.views import perfil_list, perfil_detail, perfil_delete, perfil_create, perfil_update

from aula.views import saudacaoView

app_name = 'aula'




urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view, name="primeira_view"),

    path('funcao/saudacao', views_funcoes.saudacao, name="saudacao"),

    path('funcao/teste/<str:name>', views_funcoes.teste, name="teste"),

    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),

    path('classe/saudacao', saudacaoView.as_view(), name='saudacao_view_classe'),

    path('classe/nome_classe/<str:cidade>', NomeView.as_view(), name='nome_view_classe'),

    path('class/list', PerfilListView.as_view(), name="Perfil_class_list"),

    path('class/read/<int:pk>', PerfilDetailView.as_view(), name="Perfil_class_read"),

    path('funcao/perfils', perfil_list, name='perfil_list'),

    path('function/read/<int:pk>', perfil_detail, name="perfils_function_read"),

    path('function/delete/<int:pk>', perfil_delete, name="perfils_function_delete"),

    path('function/create', perfil_create, name="aula_function_create"),

    path('function/update/<int:perfil_id>', perfil_update, name="perfils_function_update"),

    path('class/gerar_codigo/<int:pk>', CodeGenerate.as_view(), name="class_code_generator"),

    path('class/delete/<int:pk>/', PerfilDeleteView.as_view(), name="perfil_class_delete" ),

    path('class/create', PerfilCreate.as_view(), name="perfil_class_create")


]
