# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-02 02:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0003_creditcard_stripe_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='creditcard',
            name='sucurity_code',
        ),
    ]