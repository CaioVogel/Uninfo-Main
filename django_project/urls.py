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
from django.urls import path
from django.urls.conf import include
from Uninfo import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('favoritos',views.favoritos,name='favoritos'),
    path('', views.home, name='home'),
    path('inscricoes/', views.inscricao),
    path('inscricoes/sucesso/', views.inscricao_sucesso, name='sucesso'),
    path('inicial/', views.tela_principal),
    path('PUC-Rio/', views.pag_puc, name='pag_puc'),
    path('UERJ/', views.pag_uerj, name='pag_uerj'),
    path('UFRJ/', views.pag_ufrj, name='pag_ufrj'),
    path('accounts/', include('accounts.urls')),
    path('cadastro_atividade/', views.adicionar_atividade, name='cadastro_atividade'),
    path('cursos/', views.pag_cursos, name = 'pag_cursos')
]
