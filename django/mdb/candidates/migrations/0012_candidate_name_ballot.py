# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0011_auto_20160821_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='name_ballot',
            field=models.CharField(default=1, max_length=128, verbose_name='Nome urna'),
            preserve_default=False,
        ),
    ]
