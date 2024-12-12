from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Rotas para Filme
    path('filmes/', views.lista_filmes, name='lista_filmes'),
    path('filmes/<int:filme_id>/', views.detalhe_filme, name='detalhe_filme'),
    path('filmes/novo/', views.criar_filme, name='criar_filme'),
    path('filmes/<int:filme_id>/editar/', views.atualizar_filme, name='atualizar_filme'),
    path('filmes/<int:filme_id>/deletar/', views.deletar_filme, name='deletar_filme'),

    # Rotas para Ator
    path('atores/', views.lista_atores, name='lista_atores'),
    path('atores/<int:ator_id>/', views.detalhe_ator, name='detalhe_ator'),
    path('atores/novo/', views.criar_ator, name='criar_ator'),
    path('atores/<int:ator_id>/editar/', views.atualizar_ator, name='atualizar_ator'),
    path('atores/<int:ator_id>/deletar/', views.deletar_ator, name='deletar_ator'),

    # Rotas para Categoria
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:categoria_id>/', views.detalhe_categoria, name='detalhe_categoria'),
    path('categorias/novo/', views.criar_categoria, name='criar_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.atualizar_categoria, name='atualizar_categoria'),
    path('categorias/<int:categoria_id>/deletar/', views.deletar_categoria, name='deletar_categoria'),
    # Rotas para Plataforma
    path('plataformas/', views.lista_plataformas, name='lista_plataformas'),
    path('plataformas/<int:plataforma_id>/', views.detalhe_plataforma, name='detalhe_plataforma'),
    path('plataformas/novo/', views.criar_plataforma, name='criar_plataforma'),
    path('plataformas/<int:plataforma_id>/editar/', views.atualizar_plataforma, name='atualizar_plataforma'),
    path('plataformas/<int:plataforma_id>/deletar/', views.deletar_plataforma, name='deletar_plataforma'),

    # Rotas para Ingresso
    path('ingressos/', views.lista_ingressos, name='lista_ingressos'),
    path('ingressos/<int:ingresso_id>/', views.detalhe_ingresso, name='detalhe_ingresso'),
    path('ingressos/novo/', views.criar_ingresso, name='criar_ingresso'),
    path('ingressos/<int:ingresso_id>/editar/', views.atualizar_ingresso, name='atualizar_ingresso'),
    path('ingressos/<int:ingresso_id>/deletar/', views.deletar_ingresso, name='deletar_ingresso'),

    # Rotas para Avaliacao
    path('avaliacoes/', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacoes/<int:avaliacao_id>/', views.detalhe_avaliacao, name='detalhe_avaliacao'),
    path('avaliacoes/novo/', views.criar_avaliacao, name='criar_avaliacao'),
    path('avaliacoes/<int:avaliacao_id>/editar/', views.atualizar_avaliacao, name='atualizar_avaliacao'),
    path('avaliacoes/<int:avaliacao_id>/deletar/', views.deletar_avaliacao, name='deletar_avaliacao'),

    # Rotas para Usuario
    path('usuarios/<int:usuario_id>/', views.detalhe_usuario, name='detalhe_usuario'),
    path('usuarios/<int:usuario_id>/editar/', views.atualizar_usuario, name='atualizar_usuario'),
    path('usuarios/<int:usuario_id>/deletar/', views.deletar_usuario, name='deletar_usuario'),
]