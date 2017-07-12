from django.contrib import admin
from outros.models import Estado, Produto
from mesas.models import Comanda
from pedidos.models import Item


admin.site.register(Estado)
admin.site.register(Comanda)
admin.site.register(Produto)
admin.site.register(Item)