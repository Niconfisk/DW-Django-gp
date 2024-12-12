from django import forms
from django.contrib.auth.models import User
from .models import Filme, Ator, Categoria, Plataforma, Ingresso, Avaliacao

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'descricao', 'duracao', 'data_lancamento', 'categorias', 'atores']

class AtorForm(forms.ModelForm):
    class Meta:
        model = Ator
        fields = ['nome', 'data_nascimento', 'biografia']
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nome', 'filmes']

class IngressoForm(forms.ModelForm):
    class Meta:
        model = Ingresso
        fields = ['filme', 'usuario', 'preco']

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['usuario', 'filme', 'nota', 'comentario']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
