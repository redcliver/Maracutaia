from django.shortcuts import render
from pedidos.models import Espeto, Bebida, Porcao, Sobremesa, Acompanhamento


# Create your views here.
def outros(request):
    
    return render(request, 'outros.html', {'title':'Outros'})

def addespeto(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        novo_espeto = Espeto(id=id, nome=nome, preco=preco)
        novo_espeto.save()
        msg = "Espeto salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'espetos/addespeto.html', {'title':'Adicionar Espeto'})

def editespetos(request):
    if request.method == 'POST':
        espeto1 = request.POST.get('espeto')
        espetos = Espeto.objects.filter(nome__icontains=espeto1).order_by('id')
        return render(request, 'espetos/editespeto.html', {'title':'Edita espeto', 'espetos':espetos})
    return render(request, 'espetos/editespeto.html', {'title':'Edita espeto'})

def editespetos1(request):
    espeto_id = request.GET.get('espeto_id')
    espeto = Espeto.objects.get(id=espeto_id)
    if request.method == 'POST':
        espeto_nome = request.POST.get('nome')
        espeto_preco = request.POST.get('preco')
        espeto.nome = espeto_nome
        espeto.preco = espeto_preco
        espeto.save()
        msg = "Espeto editada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'espetos/editespetos1.html', {'title':'Edita bebida', 'espeto':espeto})

def addbebida(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        nova_bebida = Bebida(id=id, nome=nome, preco=preco)
        nova_bebida.save()
        msg = "Bebida salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'bebidas/addbebida.html', {'title':'Adicionar Espeto'})

def editbebidas(request):
    if request.method == 'POST':
        bebida1 = request.POST.get('bebida')
        bebidas = Bebida.objects.filter(nome__icontains=bebida1).order_by('id')
        return render(request, 'bebidas/editbebida.html', {'title':'Edita bebida', 'bebidas':bebidas})
    return render(request, 'bebidas/editbebida.html', {'title':'Edita bebida'})

def editbebidas1(request):
    bebida_id = request.GET.get('bebida_id')
    bebida = Bebida.objects.get(id=bebida_id)
    if request.method == 'POST':
        bebida_nome = request.POST.get('nome')
        bebida_preco = request.POST.get('preco')
        bebida.nome = bebida_nome
        bebida.preco = bebida_preco
        bebida.save()
        msg = "Bebida editada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'bebidas/editbebida1.html', {'title':'Edita bebida', 'bebida':bebida})

def addprocao(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        nova_porcao = Porcao(id=id, nome=nome, preco=preco)
        nova_porcao.save()
        msg = "Porção salvo com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'porcoes/addporcao.html', {'title':'Adicionar Porção'})

def editporcao(request):
    if request.method == 'POST':
        porcao1 = request.POST.get('porcao')
        porcoes = Porcao.objects.filter(nome__icontains=porcao1).order_by('id')
        return render(request, 'porcoes/editporcao.html', {'title':'Edita porção', 'porcoes':porcoes})
    return render(request, 'porcoes/editporcao.html', {'title':'Edita porção'})

def editporcao1(request):
    porcao_id = request.GET.get('porcao_id')
    porcao = Porcao.objects.get(id=porcao_id)
    if request.method == 'POST':
        porcao_nome = request.POST.get('nome')
        porcao_preco = request.POST.get('preco')
        porcao.nome = porcao_nome
        porcao.preco = porcao_preco
        porcao.save()
        msg = "Porção editada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'porcoes/editporcao1.html', {'title':'Edita bebida', 'porcao':porcao})
    
def addsobremesa(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        nova_sobremesa = Sobremesa(id=id, nome=nome, preco=preco)
        nova_sobremesa.save()
        msg = "Sobremesa salva com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'sobremesa/addsobremesa.html', {'title':'Adicionar Sobremesa'})

def editsobremesa(request):
    if request.method == 'POST':
        sobremesa1 = request.POST.get('sobremesa')
        sobremesas = Sobremesa.objects.filter(nome__icontains=sobremesa1).order_by('id')
        return render(request, 'sobremesa/editsobremesa.html', {'title':'Edita sobremesa', 'sobremesas':sobremesas})
    return render(request, 'sobremesa/editsobremesa.html', {'title':'Edita sobremesa'})

def editsobremesa1(request):
    sobremesa_id = request.GET.get('sobremesa_id')
    sobremesa = Sobremesa.objects.get(id=sobremesa_id)
    if request.method == 'POST':
        sobremesa_nome = request.POST.get('nome')
        sobremesa_preco = request.POST.get('preco')
        sobremesa.nome = sobremesa_nome
        sobremesa.preco = sobremesa_preco
        sobremesa.save()
        msg = "Sobremesa editada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'sobremesa/editsobremesa1.html', {'title':'Edita sobremesa', 'sobremesa':sobremesa})

def addacomp(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        novo_acomp = Acompanhamento(id=id, nome=nome, preco=preco)
        novo_acomp.save()
        msg = "Acompanhamento salva com sucesso!"
        return render(request, 'home/home.html',{'title':'Home', 'msg':msg})
    return render(request, 'acompanhamento/addacomp.html', {'title':'Adicionar Acompanhamento'})

def editacomp(request):
    if request.method == 'POST':
        acomp1 = request.POST.get('acomp')
        acompanhamentos = Acompanhamento.objects.filter(nome__icontains=acomp1).order_by('id')
        return render(request, 'acompanhamento/editacomp.html', {'title':'Edita acompanhamento', 'acompanhamentos':acompanhamentos})
    return render(request, 'acompanhamento/editacomp.html', {'title':'Edita acompanhamento'})

def editacomp1(request):
    acomp_id = request.GET.get('acomp_id')
    acomp = Acompanhamento.objects.get(id=acomp_id)
    if request.method == 'POST':
        acomp_nome = request.POST.get('nome')
        acomp_preco = request.POST.get('preco')
        acomp.nome = acomp_nome
        acomp.preco = acomp_preco
        acomp.save()
        msg = "Sobremesa editada com sucesso!"
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    return render(request, 'acompanhamento/editacomp1.html', {'title':'Edita acompanhamento', 'acomp':acomp})