from django.urls import path
from . import views

app_name="tienda"
urlpatterns = [
    path('Lista/', views.listaArt,name="lista"),
    path('Detalle/', views.detalleArt,name="detalle"),
]
