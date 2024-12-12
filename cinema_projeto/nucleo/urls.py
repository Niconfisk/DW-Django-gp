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
]