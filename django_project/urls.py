"""
URL configuration for django_project project.

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
from django.contrib import admin
from django.urls import path, include
from Uninfo import views as U1
from uninfo import views as U2 
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favoritos/', U1.favoritos,name='favoritos'),
    path('', U1.home, name='home'),
    path('inscricoes/', U1.inscricao),
    path('inscricoes/sucesso/', U1.inscricao_sucesso, name='sucesso'),
    path('inicial/', U1.tela_principal),
    path('PUC-Rio/', U1.pag_puc, name='pag_puc'),
    path('UERJ/', U1.pag_uerj, name='pag_uerj'),
    path('UFRJ/', U1.pag_ufrj, name='pag_ufrj'),
    path('accounts/', include('accounts.urls')),
    path('cadastro_atividade/', U1.adicionar_atividade, name='cadastro_atividade'),
    path('cursos/', U1.pag_cursos, name='pag_cursos'),
    path('comment/<str:Name>/', U2.adicionar_comment, name='adicionar_comment'),
    path('Remover/<str:id>/', U2.Remover_comment, name='remover_comment'),
    path('Editar/<str:id>/', U2.Editar_comment, name='editar_comment'),
]

