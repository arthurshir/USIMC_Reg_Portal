# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-31 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0034_remove_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='minutes',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='min'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='seconds',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='sec'),
        ),
    ]
