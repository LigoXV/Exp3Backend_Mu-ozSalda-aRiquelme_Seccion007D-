from django import forms
from django.forms import ModelForm,widgets
from .models import Sugerencias, Categoria

class SugerenciasForm(ModelForm):
    class Meta:
        model = Sugerencias
        fields = ['nombre','email','telefono','categoria','textosugerencia']
        labels={
            'nombre':'Nombre',
            'email':'Email',
            'telefono':'Telefono',
            'categoria':'Categoria',
            'textosugerencia':'Textosugerencia'
        }

        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'nombre',
                    'id': 'nombre',
                    'placeholder': 'Nombre de usuario'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Nombre@dominio.cl'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': 'Número de contacto',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'categoria',
                }
            ),
            'textosugerencia': forms.Textarea(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'textosugerencia',
                    'placeholder': 'Escriba aqui su sugerencia',
                }
            ),
         
        }
