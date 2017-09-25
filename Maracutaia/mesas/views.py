from django.shortcuts import render


# Create your views here.
def mesas(request):
    return render(request, 'mesas.html', {'title':'Mesas'})
    
def detalhe(request):
    numero = request.GET.get('mesa')
    return render(request, 'detalhe.html', {'title':'Mesas'})