from django.shortcuts import render
from mesas.models import Comanda



# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def selecionaMesa(request):
    mesas =  Comanda.objects.values_list('mesa', flat=True).filter(estado__estado__contains="Aberto")
    return render(request, 'mesa.html', {'title':'Selecione a Mesa', 'mesas':mesas})

def add(request):
    return render(request, 'addpedidos.html', {'title':'Pedidos'})

def abrir(request):
    mesas =  Comanda.objects.values_list('mesa', flat=True).filter(estado__estado__contains="Fechado")
    return render(request, 'abrir.html', {'title':'Selecione a Mesa', 'mesas':mesas})

def fechar(request):
    mesas =  Comanda.objects.values_list('mesa', flat=True).filter(estado__estado__contains="Aberto")
    return render(request, 'fechar.html', {'title':'Selecione a Mesa', 'mesas':mesas})