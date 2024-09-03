from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email', 'data_cadastro')
    search_fields = ('nome', 'matricula', 'email')
    list_filter = ('data_cadastro',)

