from django.shortcuts import render, get_object_or_404, redirect
from uninfo.models import Post, comment
from uninfo.forms import PostForm, CommentForm

def inicio(request):
  post = Post.objects.all()
  Comment = comment.objects.all()

  return render(request, 'comentarios.html',{'post':post,'Comment':Comment})

def adicionar_comment(request, Name):
  post = get_object_or_404(Post, name=Name)
  formulario = CommentForm()
  if request.method == 'POST':
      formulario = CommentForm(request.POST)
      if formulario.is_valid():
          nova_referencia = formulario.save(commit=False)
          nova_referencia.usuario = request.user
          nova_referencia.post = post 
          nova_referencia.save()
          return redirect("/")
  return render(request, "Adicionar_comment.html", {'formulario': formulario, 'post': post})

def Remover_comment(request, id):
  Comment = get_object_or_404(comment, id=id) 
  if request.method == 'POST' and request.POST:
    Comment.delete()
    return redirect("/")
  return render(request, "Remover_comment.html", {'Comment':Comment})

def Editar_comment(request, id):
  Comment = get_object_or_404(comment, id=id) 
  formulario = CommentForm(instance=Comment)
  if request.method == 'POST' and request.POST:
    formulario = CommentForm(request.POST,instance=Comment)
    if formulario.is_valid():
      formulario.save()
      return redirect("/")
  return render(request,"Editar_comment.html",{'formulario':formulario}) 