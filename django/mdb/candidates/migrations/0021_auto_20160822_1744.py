# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0020_auto_20160822_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='agenda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.Agenda', verbose_name='Pauta'),
        ),
    ]
