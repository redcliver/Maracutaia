# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0004_auto_20170920_1603'),
        ('pedidos', '0002_auto_20170711_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('A', 'Aberta'), ('F', 'Fechada')], max_length=1)),
                ('mesa', models.IntegerField()),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Espeto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='item_acomp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acomp_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Acompanhamento')),
            ],
        ),
        migrations.CreateModel(
            name='item_bebida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('copos', models.IntegerField(default=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bebida_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Bebida')),
            ],
        ),
        migrations.CreateModel(
            name='item_espeto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('espeto_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Espeto')),
            ],
        ),
        migrations.CreateModel(
            name='item_porcao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='item_sobremesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Porcao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sobremesa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='produto',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='item_sobremesa',
            name='sobremesa_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Sobremesa'),
        ),
        migrations.AddField(
            model_name='item_porcao',
            name='porcao_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Porcao'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='acompanhamentos',
            field=models.ManyToManyField(to='pedidos.item_acomp'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='bebidas',
            field=models.ManyToManyField(to='pedidos.item_bebida'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='espetos',
            field=models.ManyToManyField(to='pedidos.item_espeto'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='porcoes',
            field=models.ManyToManyField(to='pedidos.item_porcao'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='sobremesas',
            field=models.ManyToManyField(to='pedidos.item_sobremesa'),
        ),
    ]