# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-17 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0038_auto_20170430_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
    ]