from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Filme, Ator, Categoria, Plataforma, Ingresso, Avaliacao
from .forms import (
    FilmeForm, AtorForm, CategoriaForm, PlataformaForm, IngressoForm, AvaliacaoForm, UsuarioForm
)

# View para página inicial
def index(request):
    return render(request, 'base.html')

# CRUD para Filme
def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filme/lista.html', {'filmes': filmes})

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    return render(request, 'filme/detalhe.html', {'filme': filme})

@login_required
def criar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filme/form.html', {'form': form})

@login_required
def atualizar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'filme/form.html', {'form': form})

@login_required
def deletar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        filme.delete()
        return redirect('lista_filmes')
    return render(request, 'filme/confirm_delete.html', {'filme': filme})

# CRUD para Ator
def lista_atores(request):
    atores = Ator.objects.all()
    return render(request, 'ator/lista.html', {'atores': atores})

def detalhe_ator(request, ator_id):
    ator = get_object_or_404(Ator, id=ator_id)
    return render(request, 'ator/detalhe.html', {'ator': ator})

@login_required
def criar_ator(request):
    if request.method == 'POST':
        form = AtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atores')
    else:
        form = AtorForm()
    return render(request, 'ator/form.html', {'form': form})

@login_required
def atualizar_ator(request, ator_id):
    ator = get_object_or_404(Ator, id=ator_id)
    if request.method == 'POST':
        form = AtorForm(request.POST, instance=ator)
        if form.is_valid():
            form.save()
            return redirect('lista_atores')
    else:
        form = AtorForm(instance=ator)
    return render(request, 'ator/form.html', {'form': form})

@login_required
def deletar_ator(request, ator_id):
    ator = get_object_or_404(Ator, id=ator_id)
    if request.method == 'POST':
        ator.delete()
        return redirect('lista_atores')
    return render(request, 'ator/confirm_delete.html', {'ator': ator})

# CRUD para Categoria
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/lista.html', {'categorias': categorias})

def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, 'categoria/detalhe.html', {'categoria': categoria})

@login_required
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/form.html', {'form': form})

@login_required
def atualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/form.html', {'form': form})

@login_required
def deletar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categoria/confirm_delete.html', {'categoria': categoria})
