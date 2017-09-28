from django.shortcuts import render

import ctypes
# Create your views here.
def home(request):
    msg = "Bom Trabalho!"
    return render(request, 'home/home.html', {'title':'Home', 'msg':msg})