# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_watchlistitem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlistitem',
            unique_together=set([('movie', 'user')]),
        ),
    ]
