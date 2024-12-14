from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Filme, Ator, Categoria, Plataforma, Ingresso, Avaliacao
from .forms import (
    FilmeForm, AtorForm, CategoriaForm, PlataformaForm, IngressoForm, AvaliacaoForm, UsuarioForm
)

# Página inicial
def index(request):
    return render(request, 'base.html')

# Filme
class FilmeListView(ListView):
    model = Filme
    template_name = 'filme/lista.html'
    context_object_name = 'filmes'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme/detalhe.html'
    context_object_name = 'filme'

class FilmeCreateView(LoginRequiredMixin, CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/form.html'
    success_url = reverse_lazy('lista_filmes')

class FilmeUpdateView(LoginRequiredMixin, UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/form.html'
    success_url = reverse_lazy('lista_filmes')

class FilmeDeleteView(LoginRequiredMixin, DeleteView):
    model = Filme
    template_name = 'filme/confirm_delete.html'
    success_url = reverse_lazy('lista_filmes')

# Ator
class AtorListView(ListView):
    model = Ator
    template_name = 'ator/lista.html'
    context_object_name = 'atores'

class AtorDetailView(DetailView):
    model = Ator
    template_name = 'ator/detalhe.html'
    context_object_name = 'ator'

class AtorCreateView(LoginRequiredMixin, CreateView):
    model = Ator
    form_class = AtorForm
    template_name = 'ator/form.html'
    success_url = reverse_lazy('lista_atores')

class AtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Ator
    form_class = AtorForm
    template_name = 'ator/form.html'
    success_url = reverse_lazy('lista_atores')

class AtorDeleteView(LoginRequiredMixin, DeleteView):
    model = Ator
    template_name = 'ator/confirm_delete.html'
    success_url = reverse_lazy('lista_atores')

# Categoria
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/lista.html'
    context_object_name = 'categorias'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria/detalhe.html'
    context_object_name = 'categoria'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/form.html'
    success_url = reverse_lazy('lista_categorias')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/form.html'
    success_url = reverse_lazy('lista_categorias')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria/confirm_delete.html'
    success_url = reverse_lazy('lista_categorias')

# Plataforma
class PlataformaListView(ListView):
    model = Plataforma
    template_name = 'plataforma/lista.html'
    context_object_name = 'plataformas'

class PlataformaDetailView(DetailView):
    model = Plataforma
    template_name = 'plataforma/detalhe.html'
    context_object_name = 'plataforma'

class PlataformaCreateView(LoginRequiredMixin, CreateView):
    model = Plataforma
    form_class = PlataformaForm
    template_name = 'plataforma/form.html'
    success_url = reverse_lazy('lista_plataformas')

class PlataformaUpdateView(LoginRequiredMixin, UpdateView):
    model = Plataforma
    form_class = PlataformaForm
    template_name = 'plataforma/form.html'
    success_url = reverse_lazy('lista_plataformas')

class PlataformaDeleteView(LoginRequiredMixin, DeleteView):
    model = Plataforma
    template_name = 'plataforma/confirm_delete.html'
    success_url = reverse_lazy('lista_plataformas')

# Ingresso
class IngressoListView(ListView):
    model = Ingresso
    template_name = 'ingresso/lista.html'
    context_object_name = 'ingressos'

class IngressoDetailView(DetailView):
    model = Ingresso
    template_name = 'ingresso/detalhe.html'
    context_object_name = 'ingresso'

class IngressoCreateView(LoginRequiredMixin, CreateView):
    model = Ingresso
    form_class = IngressoForm
    template_name = 'ingresso/form.html'
    success_url = reverse_lazy('lista_ingressos')

class IngressoUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingresso
    form_class = IngressoForm
    template_name = 'ingresso/form.html'
    success_url = reverse_lazy('lista_ingressos')

class IngressoDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingresso
    template_name = 'ingresso/confirm_delete.html'
    success_url = reverse_lazy('lista_ingressos')

# Avaliacao
class AvaliacaoListView(ListView):
    model = Avaliacao
    template_name = 'avaliacao/lista.html'
    context_object_name = 'avaliacoes'

class AvaliacaoDetailView(DetailView):
    model = Avaliacao
    template_name = 'avaliacao/detalhe.html'
    context_object_name = 'avaliacao'

class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao/form.html'
    success_url = reverse_lazy('lista_avaliacoes')

class AvaliacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao/form.html'
    success_url = reverse_lazy('lista_avaliacoes')

class AvaliacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    template_name = 'avaliacao/confirm_delete.html'
    success_url = reverse_lazy('lista_avaliacoes')

# Autenticação
class UserLoginView(LoginView):
    template_name = 'auth/login.html'

def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('index') 
    
    logout(request)
    return redirect('user_login')

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('lista_filmes')

    def form_valid(self, form):
        # Verifica se o nome de usuário já existe antes de tentar salvar
        username = form.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'Este nome de usuário já está em uso.')
            return self.form_invalid(form)

        # Se o nome de usuário não existe, salva o usuário normalmente
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = 'usuario/form.html'
    success_url = reverse_lazy('index')
