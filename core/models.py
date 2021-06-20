from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre del tipo de sugerencia')

    def __str__(self):
        return(self.nombreCategoria)

class Sugerencias(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre de usuario')
    email = models.CharField(max_length=100, verbose_name='Correo Electronico')
    telefono = models.CharField(max_length=9, verbose_name='Número de contacto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    textosugerencia = models.CharField(max_length=500, verbose_name="Que nos quiere comentar?")

    def __str__(self):
        return(self.nombre)





