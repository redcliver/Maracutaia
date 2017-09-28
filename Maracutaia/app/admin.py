from django.contrib import admin
from outros.models import Estado, Produto
from pedidos.models import Comanda


admin.site.register(Estado)
admin.site.register(Produto)
admin.site.register(Comanda)