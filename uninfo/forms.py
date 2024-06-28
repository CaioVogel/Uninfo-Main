from django import forms
from uninfo.models import Post,comment

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['name','description']

class CommentForm(forms.ModelForm):
  class Meta:
      model = comment
      fields = ['name', 'body']