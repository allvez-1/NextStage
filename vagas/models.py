from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    requisitos = models.TextField()
    bolsa = models.CharField(max_length=100, blank=True)
    prazo = models.DateField()

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Candidatura(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    curso = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)

    curriculo = models.FileField(upload_to='curriculos/')

    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome