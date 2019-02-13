# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Phoneinfo(models.Model):
    mobile_name = models.CharField(u'手机名称',max_length=64)
    ios_or_andriod = (
        (0,'ios'),
        (1,'andriod')
    )
    phone_type = models.IntegerField(choices=ios_or_andriod,default=1)
    resolution_rate = models.CharField(u'手机分辨率',max_length=20)
    system_name = models.CharField(u'系统型号', max_length=10)
    comprehensive_screen = (
        (0,'否'),
        (1,'是')
    )
    is_comprehensive_screen = models.IntegerField(choices=comprehensive_screen,default=0)
    finger_print = (
        (0,'否'),
        (1,'是')
    )
    is_finger_print = models.IntegerField(choices=finger_print,default=0)
    borrow_status = (
        (0,'未借出'),
        (1,'已借出')
    )
    status = models.IntegerField(choices=borrow_status,default=0)
    pic_url = models.CharField(u'图片上传路径', max_length=200, blank=True)
    create_time = models.DateTimeField(u'创建时间',auto_now=True)
    equip_status = (
        (0,'可用'),
        (1,'不可用')
    )
    yn = models.IntegerField(choices=equip_status,default=0)

    class Meta:
        verbose_name = u'手机信息'
        verbose_name_plural = u'手机信息'

    def __str__(self):
        return self.mobile_name

class Borrow_record_info(models.Model):
    borrow_mobile = models.ForeignKey('Phoneinfo',on_delete=models.CASCADE,default='')
    borrow_person = models.CharField(u'借出人',max_length=20,default='')
    borrow_department = models.CharField(u'借出人部门',max_length=20,null=True)
    borrow_time = models.DateTimeField(u'借出时间', auto_now=True)
    back_time = models.CharField(u'归还时间',max_length=40,null=True,blank=True)
    status = (
        (0,u'已归还'),
        (1,u'未归还')
    )
    borrow_status = models.IntegerField(choices = status,default=1)
    borrow_remark = models.CharField(u'备注',max_length=20,null=True,default='')
    class Meta:
        verbose_name = u'借还记录'
        verbose_name_plural = u'借还记录'

    def __str__(self):
        return self.borrow_person