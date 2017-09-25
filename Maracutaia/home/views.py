from django.shortcuts import render
from escpos.serial import SerialConnection
from escpos.impl.epson import GenericESCPOS
from escpos.impl.bematech import MP4200TH
# Create your views here.
def home(request):
    msg = "Bom Trabalho!"
    return render(request, 'home/home.html', {'title':'Home', 'msg':msg})