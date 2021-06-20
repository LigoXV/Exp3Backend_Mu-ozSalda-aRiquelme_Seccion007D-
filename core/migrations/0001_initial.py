# Generated by Django 3.2.3 on 2021-06-20 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre del tipo de sugerencia')),
            ],
        ),
        migrations.CreateModel(
            name='Sugerencias',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre de usuario')),
                ('email', models.CharField(max_length=100, verbose_name='Correo Electronico')),
                ('telefono', models.CharField(max_length=9, verbose_name='Número de contacto')),
                ('textosugerencia', models.CharField(max_length=500, verbose_name='Que nos quiere comentar?')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]