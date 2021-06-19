from django.shortcuts import render

# Create your views here.
def paginaprincipal(request):
    return render(request, 'Pagina principal.html')

def galeria(request):
    return render(request, 'Galeria de fotos.html')

def sugerencias(request):
    return render(request, 'core/Sugerencias.html')

