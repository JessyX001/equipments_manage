# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-25 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneinfo', '0013_auto_20181024_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneinfo',
            name='yn',
            field=models.IntegerField(choices=[(0, '\u53ef\u7528'), (1, '\u4e0d\u53ef\u7528')], default=0),
        ),
    ]
