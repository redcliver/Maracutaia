from django.db import models
from outros.models import Produto

# Create your models here.
class Item(models.Model):
    produto = models.ForeignKey(Produto)
    quantidade = models.IntegerField()
    obs = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.produto.nome
