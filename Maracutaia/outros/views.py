from django.shortcuts import render, HttpResponseRedirect
from .models import Produto, ProdutoForm


# Create your views here.
def outros(request):
    
    return render(request, 'outros.html', {'title':'Outros'})

def addproduto(request):
    if request.method == "GET":
        form = ProdutoForm()
        return render(request, 'addproduto.html', { 'form':form, 'title':'Adicionar Produto'})
    elif request.method == "POST":
        form = ProdutoForm(request.POST)
        form.save()
        msg = "Produto adicionado com sucesso!"
        return HttpResponseRedirect('/home', {'msg':msg})