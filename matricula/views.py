from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

def index(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunosCadastrados')
    else:
        form = AlunoForm()
    context = {'form': form}

    return render(request, 'index.html', context)
    
def alunosCadastrados(request):
    context = {'cadastrados': Aluno.objects.all()}
    return render(request, 'alunos_cadastrados.html', context)
