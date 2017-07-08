from django.db import models
from django import forms

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nome

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto;
        fields = ['nome', 'preco', 'descricao']