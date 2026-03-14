from django import forms
from .models import Vaga, Candidatura


class VagaForm(forms.ModelForm):

    class Meta:
        model = Vaga
        fields = [
            'titulo',
            'descricao',
            'requisitos',
            'bolsa',
            'prazo',
            'empresa'
        ]


class CandidaturaForm(forms.ModelForm):

    class Meta:
        model = Candidatura
        fields = [
            'nome',
            'email',
            'telefone',
            'curso',
            'instituicao',
            'curriculo'
        ]