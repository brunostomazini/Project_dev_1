from manage import *
import contextlib, io

saida = io.StringIO()
with contextlib.redirect_stdout(saida):
    main()
#Imports

from datetime import *
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from relacionamentos.models import Article, Magazine, Reporter


'''User = get_user_model()
User.objects.create_superuser('ifrs', '', 'ifrs')'''

def insere_dados_inicias():

    reporter = Reporter(name="Teste da silva",cpf="85928020082",email="teste.s@gmail.com")
    reporter.full_clean()
    reporter.save()

    magazine = Magazine(nome="RevisTeste",edicao="99")
    magazine.full_clean()
    magazine.save()

    artigo = Article(titulo="Testando",
                     pub_date=date.today(),
                     reporter=reporter)
    artigo.full_clean()
    artigo.save()
    artigo.magazines.add(magazine)
    artigo.save()

insere_dados_inicias()

'''def inserir():
    reporter = Reporter(name=input(), cpf=input(), email=input())
    reporter.full_clean()
    reporter.save()

def retornar():
    pass

def atualizar():
    pass

def deletar():
    pass'''