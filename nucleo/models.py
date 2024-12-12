from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ator(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    biografia = models.TextField()

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.DurationField()
    data_lancamento = models.DateField()
    categorias = models.ManyToManyField(Categoria)
    atores = models.ManyToManyField(Ator)

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField(max_length=50)
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Ingresso de {self.usuario} para {self.filme}"

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Avaliação de {self.usuario} para {self.filme}"
    
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
