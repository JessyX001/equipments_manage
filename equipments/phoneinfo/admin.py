# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from phoneinfo.models import Phoneinfo
from phoneinfo.models import Borrow_record_info

# Register your models here.

# @admin.register(Phoneinfo)
class PhoneinfoAdmin(admin.ModelAdmin):
    list_display = ['mobile_name','ios_or_andriod','resolution_rate','system_name','is_comprehensive_screen','is_finger_print','status','create_time']
    list_per_page = 10

    actions_on_top = True
    actions_on_bottom = True

    empty_value_display = '-空-'

    list_editable = ['resolution_rate','system_name']

    list_filter = ['ios_or_andriod','is_comprehensive_screen','is_finger_print','status']

    search_fields = ['ios_or_andriod','is_comprehensive_screen','is_finger_print','status']

admin.site.register(Phoneinfo)


class Borrow_record_info_Admin(admin.ModelAdmin):
    list_display = ['borrow_person','borrow_department','borrow_time','return_time']

admin.site.register(Borrow_record_info)

admin.site.site_title = '手机设备管理平台'
admin.site.site_header = '手机设备管理平台'