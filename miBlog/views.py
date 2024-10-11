from django.shortcuts import render

# Create your views here.
def listaArt(request):
    return render(request, 'lista_articulos.html')


def detalleArt(request):
    return render(request, 'detalle_articulo.html')