# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20161214_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='private_comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tags',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='zendesk_ticket_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]