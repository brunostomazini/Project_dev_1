from django.urls import path
from services.views import *
from .serialiazers import CalculoSerialiazer




app_name = 'services'

urlpatterns = [

    path('', api_root, name="api-root"),

    path('saudacao', saudacao, name="saudacao"),

    path('saudacao/classe', SaudacaoClass.as_view(), name="saudacao_class"),

    path('calculo', calculo, name="calculo")

]