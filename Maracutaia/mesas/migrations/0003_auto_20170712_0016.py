# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 04:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesas', '0002_auto_20170711_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 12, 0, 16, 19, 957658)),
        ),
    ]