from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    TIPO_USUARIO = (
        ('estudante','Estudante'),
        ('empresa','Empresa'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)
    area = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)