from django.shortcuts import render
from outros.models import Produto
# Create your views here.
def pedidos(request):
    return render(request, 'pedidos.html', {'title':'Pedidos'})

def addpedidos(request):
    numero = request.GET.get('mesa')
    produtos = Produto.objects.all()

    return render(request, 'addpedidos.html', {'title':'Pedidos', 'numero':numero, 'produtos':produtos})