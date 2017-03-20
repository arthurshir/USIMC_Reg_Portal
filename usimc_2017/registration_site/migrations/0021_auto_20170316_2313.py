# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-16 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0020_auto_20170313_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentcontact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='is_chinese',
            field=models.BooleanField(default=False, verbose_name='This is a Chinese Piece'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='Phone Number'),
        ),
    ]