from django.shortcuts import render

# Create your views here.
def entregas(request):
    return render(request, 'entregas.html', {'title':'Entregas'})