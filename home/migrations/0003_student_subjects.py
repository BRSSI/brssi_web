# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161229_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(to='home.Subject'),
        ),
    ]
