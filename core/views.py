from django.shortcuts import render, redirect
from .models import Sugerencias
from .forms import SugerenciasForm, creaSugerenciasForm

# Create your views here.
def paginaprincipal(request):
    return render(request, 'Pagina principal.html')

def galeria(request):
    return render(request, 'Galeria de fotos.html')

def sugerencias(request):
    if request.method=='GET':
        formulario=SugerenciasForm()
        contexto={
            'formulario':formulario
        }
    else:
        formulario=SugerenciasForm(request.POST)
        contexto={
            'formulario':formulario
        }
        if formulario.is_valid:
            formulario.save()
            return redirect('crud')

    return render(request, 'core/Sugerencias.html', {'formulario':formulario})

def crud(request):
    sugerencia=Sugerencias.objects.all()
    return render(request, 'core/crud.html', context={'every':sugerencia})

def form_mod_sugerencia(request,id):
    sugerencia = Sugerencias.objects.get(nombre=id)

    datos ={
        'form': SugerenciasForm(instance=sugerencia)
    }
    if request.method == 'POST': 
        formulario = SugerenciasForm(data=request.POST, instance = sugerencia)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('crud')
    return render(request, 'core/form_mod_sugerencia.html', datos)


def form_del_sugerencia(request,id):
    sugerencia = Sugerencias.objects.get(nombre=id)
    sugerencia.delete()
    return redirect('crud')
