# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0019_auto_20170313_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ensemblemember',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ensemblemember',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone_number',
        ),
    ]
