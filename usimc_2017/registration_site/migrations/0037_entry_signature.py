# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-04 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0036_auto_20170331_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]