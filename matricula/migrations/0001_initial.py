# Generated by Django 5.1.1 on 2024-09-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
