from django.urls import path
from .views import (
    FilmeListView, FilmeDetailView, FilmeCreateView, FilmeUpdateView, FilmeDeleteView,
    AtorListView, AtorDetailView, AtorCreateView, AtorUpdateView, AtorDeleteView,
    CategoriaListView, CategoriaDetailView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    PlataformaListView, PlataformaDetailView, PlataformaCreateView, PlataformaUpdateView, PlataformaDeleteView,
    IngressoListView, IngressoDetailView, IngressoCreateView, IngressoUpdateView, IngressoDeleteView,
    AvaliacaoListView, AvaliacaoDetailView, AvaliacaoCreateView, AvaliacaoUpdateView, AvaliacaoDeleteView,
    UserLoginView, UserRegisterView, UserUpdateView
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Filmes
    path('filmes/', FilmeListView.as_view(), name='lista_filmes'),
    path('filmes/<int:pk>/', FilmeDetailView.as_view(), name='detalhe_filme'),
    path('filmes/novo/', FilmeCreateView.as_view(), name='criar_filme'),
    path('filmes/<int:pk>/editar/', FilmeUpdateView.as_view(), name='atualizar_filme'),
    path('filmes/<int:pk>/deletar/', FilmeDeleteView.as_view(), name='deletar_filme'),

    # Atores
    path('atores/', AtorListView.as_view(), name='lista_atores'),
    path('atores/<int:pk>/', AtorDetailView.as_view(), name='detalhe_ator'),
    path('atores/novo/', AtorCreateView.as_view(), name='criar_ator'),
    path('atores/<int:pk>/editar/', AtorUpdateView.as_view(), name='atualizar_ator'),
    path('atores/<int:pk>/deletar/', AtorDeleteView.as_view(), name='deletar_ator'),

    # Categorias
    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='detalhe_categoria'),
    path('categorias/novo/', CategoriaCreateView.as_view(), name='criar_categoria'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='atualizar_categoria'),
    path('categorias/<int:pk>/deletar/', CategoriaDeleteView.as_view(), name='deletar_categoria'),

    # Plataformas
    path('plataformas/', PlataformaListView.as_view(), name='lista_plataformas'),
    path('plataformas/<int:pk>/', PlataformaDetailView.as_view(), name='detalhe_plataforma'),
    path('plataformas/novo/', PlataformaCreateView.as_view(), name='criar_plataforma'),
    path('plataformas/<int:pk>/editar/', PlataformaUpdateView.as_view(), name='atualizar_plataforma'),
    path('plataformas/<int:pk>/deletar/', PlataformaDeleteView.as_view(), name='deletar_plataforma'),

    # Ingressos
    path('ingressos/', IngressoListView.as_view(), name='lista_ingressos'),
    path('ingressos/<int:pk>/', IngressoDetailView.as_view(), name='detalhe_ingresso'),
    path('ingressos/novo/', IngressoCreateView.as_view(), name='criar_ingresso'),
    path('ingressos/<int:pk>/editar/', IngressoUpdateView.as_view(), name='atualizar_ingresso'),
    path('ingressos/<int:pk>/deletar/', IngressoDeleteView.as_view(), name='deletar_ingresso'),

    # Avaliações
    path('avaliacoes/', AvaliacaoListView.as_view(), name='lista_avaliacoes'),
    path('avaliacoes/<int:pk>/', AvaliacaoDetailView.as_view(), name='detalhe_avaliacao'),
    path('avaliacoes/novo/', AvaliacaoCreateView.as_view(), name='criar_avaliacao'),
    path('avaliacoes/<int:pk>/editar/', AvaliacaoUpdateView.as_view(), name='atualizar_avaliacao'),
    path('avaliacoes/<int:pk>/deletar/', AvaliacaoDeleteView.as_view(), name='deletar_avaliacao'),

    # Autenticação
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('registrar/', UserRegisterView.as_view(), name='user_register'),
    path('usuarios/<int:pk>/editar/', UserUpdateView.as_view(), name='atualizar_usuario'),
]