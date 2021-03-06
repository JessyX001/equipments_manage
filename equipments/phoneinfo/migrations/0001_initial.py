# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-14 02:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_record_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_person', models.CharField(default='', max_length=20, verbose_name='\u501f\u51fa\u4eba')),
                ('borrow_department', models.CharField(max_length=20, null=True, verbose_name='\u501f\u51fa\u4eba\u90e8\u95e8')),
                ('borrow_time', models.DateTimeField(auto_now=True, verbose_name='\u501f\u51fa\u65f6\u95f4')),
                ('back_time', models.CharField(blank=True, max_length=40, null=True, verbose_name='\u5f52\u8fd8\u65f6\u95f4')),
                ('borrow_status', models.IntegerField(choices=[(0, '\u5df2\u5f52\u8fd8'), (1, '\u672a\u5f52\u8fd8')], default=1)),
                ('borrow_remark', models.CharField(default='', max_length=20, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u501f\u8fd8\u8bb0\u5f55',
                'verbose_name_plural': '\u501f\u8fd8\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Phoneinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_name', models.CharField(max_length=64, verbose_name='\u624b\u673a\u540d\u79f0')),
                ('phone_type', models.IntegerField(choices=[(0, 'ios'), (1, 'andriod')], default=1)),
                ('resolution_rate', models.CharField(max_length=20, verbose_name='\u624b\u673a\u5206\u8fa8\u7387')),
                ('system_name', models.CharField(max_length=10, verbose_name='\u7cfb\u7edf\u578b\u53f7')),
                ('is_comprehensive_screen', models.IntegerField(choices=[(0, '\u5426'), (1, '\u662f')], default=0)),
                ('is_finger_print', models.IntegerField(choices=[(0, '\u5426'), (1, '\u662f')], default=0)),
                ('status', models.IntegerField(choices=[(0, '\u672a\u501f\u51fa'), (1, '\u5df2\u501f\u51fa')], default=0)),
                ('pic_url', models.CharField(blank=True, max_length=200, verbose_name='\u56fe\u7247\u4e0a\u4f20\u8def\u5f84')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('yn', models.IntegerField(choices=[(0, '\u53ef\u7528'), (1, '\u4e0d\u53ef\u7528')], default=0)),
            ],
            options={
                'verbose_name': '\u624b\u673a\u4fe1\u606f',
                'verbose_name_plural': '\u624b\u673a\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='borrow_record_info',
            name='borrow_mobile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='phoneinfo.Phoneinfo'),
        ),
    ]
