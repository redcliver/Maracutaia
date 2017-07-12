from django.shortcuts import render
from mesas.models import Comanda, Item


# Create your views here.
def mesas(request):
    return render(request, 'mesas.html', {'title':'Mesas'})
    
def detalhe(request):
    numero = request.GET.get('mesa')
    if 'mesa' in request.GET:
        comanda = Comanda.objects.all().filter(estado__estado__contains="Aberto", mesa__contains=numero)
        
        return render(request, 'detalhe.html', {'title':'Mesas', 'numero':numero ,'comanda':comanda})
    return render(request, 'detalhe.html', {'title':'Mesas', 'numero':numero,'comanda':comanda})