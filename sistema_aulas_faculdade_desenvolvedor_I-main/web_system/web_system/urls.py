"""
URL configuration for web_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from web_system.views import index
from .views import contact
from .views import ContatoView
from django.contrib.auth import views as auth_views
from web_system.forms import CustomLoginForm
from web_system.views import ProfileView




urlpatterns = [

    #path('relacionamentos/', include('relacionamentos.urls', namespace='app'),),
    path('',index, name='index'),

    path('aula/', include('aula.urls', namespace='app'),),

    path('admin/', admin.site.urls),

    path('function/contato', contact, name="funcao_contato"),

    path('class/contato', ContatoView.as_view(), name="class_contact"),

    path('accounts/login/', auth_views.LoginView.as_view(template_name = "login.html", authentication_form = CustomLoginForm), name='login'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/profile/', ProfileView.as_view(), name='profile'),

]
