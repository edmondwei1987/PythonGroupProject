# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-02 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='stripe_card',
            field=models.CharField(default='', max_length=255),
        ),
    ]