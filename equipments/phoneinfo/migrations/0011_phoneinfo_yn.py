# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-23 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneinfo', '0010_borrow_record_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneinfo',
            name='yn',
            field=models.IntegerField(choices=[(0, '\u4e0d\u53ef\u7528'), (1, '\u53ef\u7528')], default=1),
        ),
    ]