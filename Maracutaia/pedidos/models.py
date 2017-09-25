from django.db import models

# Create your models here.
class Bebida(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome

class item_bebida(models.Model):
    id = models.AutoField(primary_key=True)
    bebida_item = models.ForeignKey(Bebida)
    copos = models.IntegerField(default=1)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class Espeto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome

class item_espeto(models.Model):
    id = models.AutoField(primary_key=True)
    espeto_item = models.ForeignKey(Espeto)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class Porcao(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome

class item_porcao(models.Model):
    id = models.AutoField(primary_key=True)
    porcao_item = models.ForeignKey(Porcao)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class Acompanhamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome

class item_acomp(models.Model):
    id = models.AutoField(primary_key=True)
    acomp_item = models.ForeignKey(Acompanhamento)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class Sobremesa(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.nome

class item_sobremesa(models.Model):
    id = models.AutoField(primary_key=True)
    sobremesa_item = models.ForeignKey(Sobremesa)
    obs = models.CharField(max_length=200, null=True, blank=True)
    qnt = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class Comanda(models.Model):
    STATE = (
        ('A', 'Aberta'),
        ('F', 'Fechada'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=STATE)
    bebidas = models.ManyToManyField(item_bebida)
    espetos = models.ManyToManyField(item_espeto)
    porcoes = models.ManyToManyField(item_porcao)
    acompanhamentos = models.ManyToManyField(item_acomp)
    sobremesas = models.ManyToManyField(item_sobremesa)
    mesa = models.IntegerField()
    obs = models.CharField(max_length=200, null=True, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return str(self.id)
