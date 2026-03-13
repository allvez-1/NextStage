from django.db import models
from usuarios.models import Usuario
from vagas.models import Vaga

class Candidatura(models.Model):

    STATUS = (
        ('pendente','Pendente'),
        ('aprovado','Aprovado'),
        ('rejeitado','Rejeitado')
    )

    estudante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    curriculo = models.FileField(upload_to='curriculos/')
    status = models.CharField(max_length=20, choices=STATUS, default='pendente')

    data = models.DateTimeField(auto_now_add=True)