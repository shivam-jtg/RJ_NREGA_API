# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='timestamp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
