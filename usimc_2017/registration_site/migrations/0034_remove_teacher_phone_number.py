# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0033_auto_20170331_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='phone_number',
        ),
    ]
