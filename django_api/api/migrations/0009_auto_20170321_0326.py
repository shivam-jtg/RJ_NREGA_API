# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-21 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170321_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.AddField(
            model_name='employee',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.District'),
        ),
    ]