# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-30 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_site', '0037_entry_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='instrument_category',
            field=models.CharField(choices=[(b'cello', b'Cello'), (b'chamber_ensemble', b'Chamber Ensemble'), (b'chinese_traditional_instrument_bowed_strings', b'Bowed Strings - Chinese Traditional Instrument'), (b'chinese_traditional_instrument_guqin', b'Guqin - Chinese Traditional Instrument'), (b'chinese_traditional_instrument_plucked_string', b'Plucked String - Chinese Traditional Instrument'), (b'chinese_traditional_instrument_professional_zither', b'Professional Guzheng (Zither) - Chinese Traditional Instrument'), (b'chinese_traditional_instrument_woodwinds', b'Woodwinds - Chinese Traditional Instrument'), (b'chinese_traditional_instrument_zither', b'Guzheng (Zither) - Chinese Traditional Instrument'), (b'chinese_traditional_instruments_ensemble', b'Chinese Traditional Instruments Ensemble'), (b'clarinet', b'Clarinet'), (b'flute', b'Flute'), (b'marimba', b'Marimba'), (b'piano', b'Piano'), (b'viola', b'Viola'), (b'violin', b'Violin'), (b'vocal', b'Vocal'), (b'vocal_ensemble', b'Vocal Ensemble')], max_length=100),
        ),
    ]