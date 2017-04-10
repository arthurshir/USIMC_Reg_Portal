# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0030_auto_20170329_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='length',
        ),
        migrations.AddField(
            model_name='piece',
            name='minutes',
            field=models.IntegerField(blank=True, null=True, verbose_name='min'),
        ),
        migrations.AddField(
            model_name='piece',
            name='seconds',
            field=models.IntegerField(blank=True, null=True, verbose_name='sec'),
        ),
    ]
