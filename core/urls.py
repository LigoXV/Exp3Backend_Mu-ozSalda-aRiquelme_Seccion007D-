from django.urls import path
from .views import paginaprincipal, galeria, sugerencias

urlpatterns=[
    path('', paginaprincipal, name="paginaprincipal"),
    path('galeria/', galeria, name="galeria"),
    path('sugerencias/', sugerencias, name="sugerencias")
]