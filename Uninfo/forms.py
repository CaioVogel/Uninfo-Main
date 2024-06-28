from django import forms
from .models import Inscrito
from .models import Atividade


class InscricaoForm(forms.ModelForm):
  senha = forms.CharField(widget=forms.PasswordInput)
  class Meta:
      model = Inscrito
      fields = ['nome', 'email', 'senha']


class AtividadeForm(forms.ModelForm):
  class Meta:
      model = Atividade
      fields = ['nome', 'universidade', 'descricao', 'email_contato','link_instagram', 'link_linkedin', 'link_facebook', 'link_site_oficial']