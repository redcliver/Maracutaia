# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comanda',
            name='item',
        ),
        migrations.DeleteModel(
            name='Comanda',
        ),
    ]