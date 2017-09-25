from django.shortcuts import render
from pedidos.models import Comanda, Espeto, item_espeto


# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def selecionaMesa(request):
    mesas =  Comanda.objects.values_list('mesa', flat=True).filter(estado__estado__contains="Aberto")
    return render(request, 'mesa.html', {'title':'Selecione a Mesa', 'mesas':mesas})

def add(request):
    return render(request, 'addpedidos.html', {'title':'Pedidos'})

def abrir_mesa(request):
    mesa = request.GET.get('mesa')
    comanda_id = request.GET.get('comanda_id')
    if mesa != None or comanda_id != None:
        pedido = request.GET.get('pedido')
        if pedido == 'espetos':
            return render(request, 'espetos.html', {'title':'Espetos', 'mesa':mesa, 'comanda_id':comanda_id})
        elif pedido == 'acompanhamentos':
            return render(request, 'acompanhamentos.html', {'title':'Acompanhamentos', 'mesa':mesa})
        elif pedido == 'procoesquentes':
            return render(request, 'procoesquentes.html', {'title':'Porcoes Quentes', 'mesa':mesa})
        elif pedido == 'procoesfrias':
            return render(request, 'procoesfrias.html', {'title':'Porcoes Frias', 'mesa':mesa})
        elif pedido == 'sanduiches':
            return render(request, 'sanduiches.html', {'title':'Sanduiches', 'mesa':mesa})
        elif pedido == 'bebidas':
            return render(request, 'bebidas.html', {'title':'Bebidas', 'mesa':mesa})
        elif pedido == 'sobremesas':
            return render(request, 'sobremesas.html', {'title':'Sobremesas', 'mesa':mesa})
        return render(request, 'seleciona_item.html', {'title':'Selecione o produto', 'mesa':mesa, 'comanda_id':comanda_id})
    return render(request, 'abrir_mesa.html', {'title':'Selecione a Mesa', 'comanda_id':comanda_id})

def bovino(request):
    mesa = request.GET.get('mesa')
    comanda_id = request.GET.get('comanda_id')
    return render(request, 'espetos/bovinos.html', {'title':'Espetos Bovinos', 'mesa':mesa, 'comanda_id':comanda_id})

def frango(request):
    mesa = request.GET.get('mesa')
    return render(request, 'espetos/frango.html', {'title':'Espetos de Frango', 'mesa':mesa})

def suino(request):
    mesa = request.GET.get('mesa')
    return render(request, 'espetos/suino.html', {'title':'Espetos Suinos', 'mesa':mesa})

def carneiro(request):
    mesa = request.GET.get('mesa')
    return render(request, 'espetos/carneiro.html', {'title':'Espetos de Carneiro', 'mesa':mesa})

def peixe(request):
    mesa = request.GET.get('mesa')
    return render(request, 'espetos/peixe.html', {'title':'Espetos de Peixes', 'mesa':mesa})

def queijo(request):
    mesa = request.GET.get('mesa')
    return render(request, 'espetos/queijo.html', {'title':'Espetos de Queijo', 'mesa':mesa})

def abrir_mesa1(request):
    mesa = request.GET.get('mesa')
    comanda_id = request.GET.get('comanda_id')
    espeto = request.GET.get('espeto')
    try:
        espeto1 = Espeto.objects.get(id=espeto)
    except:
        espeto1 = None
    if espeto1 != None:
        novo_item = item_espeto(espeto_item=espeto1, total=espeto1.preco)
        novo_item.save()
        total_comanda = espeto1.preco * novo_item.qnt
        nova_comanda = Comanda(estado='A', total=total_comanda, mesa=mesa)
        nova_comanda.save()
        nova_comanda.espetos.add(novo_item)
        nova_comanda.save()
        comanda_id = nova_comanda
        espetos1 = nova_comanda.espetos.all()
        return render(request, 'abrir_mesa1.html',{'title':'Controle', 'espetos1':espetos1, 'comanda_id':comanda_id})
    return render(request, 'abrir_mesa1.html',{'title':'Controle'})

def fechar(request):
    mesas =  Comanda.objects.values_list('mesa', flat=True).filter(estado__estado__contains="Aberto")
    return render(request, 'fechar.html', {'title':'Selecione a Mesa', 'mesas':mesas})