from django.shortcuts import render, redirect
from .forms import InscricaoForm
from django.contrib.auth.decorators import login_required
from .forms import AtividadeForm
from django.urls import reverse
from .models import Inscrito, Atividade, Universidade, Curso


def home(request):
  return render(request, 'home.html')

def inscricao(request):
  if request.method == 'POST':
    form = InscricaoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('sucesso')
  else:
    form = InscricaoForm()
  return render(request, 'inscricao.html', {'form': form})

def inscricao_sucesso(request):
  return render(request, 'sucesso.html')

  
def tela_principal(request):
  universidades = Universidade.objects.all()
  return render(request, 'inicial.html',{'universidades': universidades})

def pag_puc(request):
  return render(request, 'puc.html',)

def pag_cursos(request):
  lista_cursos = Curso.objects.all()
  return render(request, 'cursos.html',{'cursos': lista_cursos})

def pag_uerj(request):
  return render(request, 'uerj.html')

def pag_ufrj(request):
  return render(request, 'ufrj.html')

def favoritos(request):
  atividades = Atividade.objects.all()
  return render(request, 'favoritos.html', {'atividades': atividades})

def adicionar_atividade(request):
  if request.method == 'POST':
      form = AtividadeForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('favoritos')
  else:
      form = AtividadeForm()
  return render(request, 'cadastro_atividade.html', {'form': form})