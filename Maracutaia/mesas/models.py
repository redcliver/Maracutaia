from django.db import models
from outros.models import Estado
from pedidos.models import Item
import datetime

# Create your models here.
class Comanda(models.Model):
    mesa = models.IntegerField()
    pedido = models.ManyToManyField(Item)
    estado = models.ForeignKey(Estado)
    data = models.DateTimeField(default=datetime.datetime.now())
    total = models.DecimalField(max_digits=5, decimal_places=2, default="0,00")

    
