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

# CRUD para Plataforma
def lista_plataformas(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'plataforma/lista.html', {'plataformas': plataformas})

def detalhe_plataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id)
    return render(request, 'plataforma/detalhe.html', {'plataforma': plataforma})

@login_required
def criar_plataforma(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_plataformas')
    else:
        form = PlataformaForm()
    return render(request, 'plataforma/form.html', {'form': form})

@login_required
def atualizar_plataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id)
    if request.method == 'POST':
        form = PlataformaForm(request.POST, instance=plataforma)
        if form.is_valid():
            form.save()
            return redirect('lista_plataformas')
    else:
        form = PlataformaForm(instance=plataforma)
    return render(request, 'plataforma/form.html', {'form': form})

@login_required
def deletar_plataforma(request, plataforma_id):
    plataforma = get_object_or_404(Plataforma, id=plataforma_id)
    if request.method == 'POST':
        plataforma.delete()
        return redirect('lista_plataformas')
    return render(request, 'plataforma/confirm_delete.html', {'plataforma': plataforma})

# CRUD para Ingresso
def lista_ingressos(request):
    ingressos = Ingresso.objects.all()
    return render(request, 'ingresso/lista.html', {'ingressos': ingressos})

def detalhe_ingresso(request, ingresso_id):
    ingresso = get_object_or_404(Ingresso, id=ingresso_id)
    return render(request, 'ingresso/detalhe.html', {'ingresso': ingresso})

@login_required
def criar_ingresso(request):
    if request.method == 'POST':
        form = IngressoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ingressos')
    else:
        form = IngressoForm()
    return render(request, 'ingresso/form.html', {'form': form})

@login_required
def atualizar_ingresso(request, ingresso_id):
    ingresso = get_object_or_404(Ingresso, id=ingresso_id)
    if request.method == 'POST':
        form = IngressoForm(request.POST, instance=ingresso)
        if form.is_valid():
            form.save()
            return redirect('lista_ingressos')
    else:
        form = IngressoForm(instance=ingresso)
    return render(request, 'ingresso/form.html', {'form': form})

@login_required
def deletar_ingresso(request, ingresso_id):
    ingresso = get_object_or_404(Ingresso, id=ingresso_id)
    if request.method == 'POST':
        ingresso.delete()
        return redirect('lista_ingressos')
    return render(request, 'ingresso/confirm_delete.html', {'ingresso': ingresso})

# CRUD para Avaliacao
def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacao/lista.html', {'avaliacoes': avaliacoes})

def detalhe_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    return render(request, 'avaliacao/detalhe.html', {'avaliacao': avaliacao})

@login_required
def criar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_avaliacoes')
    else:
        form = AvaliacaoForm()
    return render(request, 'avaliacao/form.html', {'form': form})

@login_required
def atualizar_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('lista_avaliacoes')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'avaliacao/form.html', {'form': form})
@login_required
def deletar_avaliacao(request, avaliacao_id):
    avaliacao = get_object_or_404(Avaliacao, id=avaliacao_id)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('lista_avaliacoes')
    return render(request, 'avaliacao/confirm_delete.html', {'avaliacao': avaliacao})

# CRUD para Usuario
@login_required
def detalhe_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    return render(request, 'usuario/detalhe.html', {'usuario': usuario})

@login_required
def atualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalhe_usuario', usuario_id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/form.html', {'form': form})

@login_required
def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('user_register')
    return render(request, 'usuario/confirm_delete.html', {'usuario': usuario})
