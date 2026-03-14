from django.shortcuts import render, get_object_or_404, redirect
from .models import Vaga
from .forms import VagaForm, CandidaturaForm


def lista_vagas(request):

    vagas = Vaga.objects.all()

    return render(request, 'vagas/lista_vagas.html', {
        'vagas': vagas
    })


def detalhe_vaga(request, vaga_id):

    vaga = get_object_or_404(Vaga, id=vaga_id)

    return render(request, 'vagas/detalhe_vaga.html', {
        'vaga': vaga
    })


def cadastrar_vaga(request):

    if request.method == 'POST':

        form = VagaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_vagas')

    else:
        form = VagaForm()

    return render(request, 'vagas/cadastrar_vaga.html', {
        'form': form
    })


def candidatar(request, vaga_id):

    vaga = get_object_or_404(Vaga, id=vaga_id)

    if request.method == 'POST':

        form = CandidaturaForm(request.POST, request.FILES)

        if form.is_valid():
            candidatura = form.save(commit=False)
            candidatura.vaga = vaga
            candidatura.save()

            return redirect('lista_vagas')

    else:
        form = CandidaturaForm()

    return render(request, 'vagas/candidatura.html', {
        'form': form,
        'vaga': vaga
    })