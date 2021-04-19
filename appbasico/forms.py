from django import forms
from .models import Postagem

class PostagemModelForm(forms.ModelForm):
	class Meta:
		model = Postagem
		fields = ['time', 'nome', 'post']

