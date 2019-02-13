# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from phoneinfo.models import Phoneinfo
from phoneinfo.models import Borrow_record_info
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.
def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'用户名 或 密码错误！'})
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def left(request):
    return render(request,'left.html')

@login_required
def top(request):
    return render(request,'top.html')

@login_required
def phoneinfo_manage(request):
    username = request.session.get('user','')
    phone_list = Phoneinfo.objects.exclude(yn=1)
    records_count = Phoneinfo.objects.exclude(yn=1).count()
    print (records_count)
    borrow_list = Borrow_record_info.objects.exclude(borrow_status=0)

    return render(request,'phoneinfo_manage.html',{'user':username,"searchphones":phone_list,"records_count":records_count,"borrowrecords":borrow_list})

def addphoneinfo(request):
    return render(request,'addphoneinfo.html')

# 操作成功提示
def successinfo(request):
    return render(request,'successinfo.html')

# 添加手机信息功能
@login_required
def db_addphoneinfo(request):
    if request.method == 'POST':
        mobile_name = request.POST.get('mobile_name')
        resolution_rate = request.POST.get('resolution_rate')
        system_name = request.POST.get('system_name')
        phone_type = request.POST.get('phone_type')
        status = 0
        is_comprehensive_screen = request.POST.get('is_comprehensive_screen')
        is_finger_print = request.POST.get('is_finger_print')
        pic_url = request.POST.get('pic_url')

        if mobile_name:
            if resolution_rate:
                if system_name:
                        Phoneinfo.objects.create(
                            mobile_name=mobile_name,
                            phone_type=phone_type,
                            status=status,
                            system_name=system_name,
                            resolution_rate=resolution_rate,
                            is_comprehensive_screen=is_comprehensive_screen,
                            is_finger_print=is_finger_print,
                            pic_url=pic_url
                        )
                else:
                    return render(request, 'addphoneinfo.html', {'system_name_error': '系统型号不能为空！'})
            else:
                return render(request, 'addphoneinfo.html', {'resolution_rate_error': '屏幕分辨率不能为空！'})
        else:
            return render(request, 'addphoneinfo.html', {'mobile_name_error': '手机名称不能为空！'})

    return HttpResponseRedirect('/successinfo/')

# 修改手机信息回显
def show_changephoneinfo(request,id):
    phoneinfo = Phoneinfo.objects.get(id = id)
    mobile_name = phoneinfo.mobile_name
    phone_type = phoneinfo.phone_type
    resolution_rate = phoneinfo.resolution_rate
    system_name = phoneinfo.system_name
    is_comprehensive_screen = phoneinfo.is_comprehensive_screen
    is_finger_print = phoneinfo.is_finger_print
    pic_url = phoneinfo.pic_url
    id = phoneinfo.id
    return render(request,'changephoneinfo.html',{'id':id,'mobile_name':mobile_name,'phone_type':phone_type,'resolution_rate':resolution_rate,'system_name':system_name,'is_comprehensive_screen':is_comprehensive_screen,'is_finger_print':is_finger_print,'pic_url':pic_url})

# 修改手机信息功能
@login_required
def db_changephoneinfo(request,id):
    if request.POST:
        phone_type = request.POST.get('phone_type')
        Phoneinfo.objects.filter(id=id).update(phone_type=phone_type)
        is_comprehensive_screen = request.POST.get('is_comprehensive_screen')
        Phoneinfo.objects.filter(id=id).update(is_comprehensive_screen=is_comprehensive_screen)
        is_finger_print = request.POST.get('is_finger_print')
        Phoneinfo.objects.filter(id=id).update(is_finger_print=is_finger_print)
        pic_url = request.POST.get('pic_url')
        if pic_url:
            Phoneinfo.objects.filter(id=id).update(pic_url=pic_url)
        system_name = request.POST.get('system_name')
        if system_name:
            Phoneinfo.objects.filter(id=id).update(pic_url=system_name)
        resolution_rate = request.POST.get('resolution_rate')
        if resolution_rate:
            Phoneinfo.objects.filter(id=id).update(pic_url=resolution_rate)
    return HttpResponseRedirect('/successinfo/')

# 删除手机记录
@login_required
@csrf_exempt
def db_deletephoneinfo(request):
    if request.POST:
        id = request.POST['id']
        print id
        Phoneinfo.objects.filter(id = id).update(yn = 1)
        return  HttpResponse("SUCCESS")

# 借出手机填写
def show_borrowphoneinfo(request,id):
    phoneinfo = Phoneinfo.objects.get(id = id)
    borrow_mobile_name = phoneinfo.mobile_name
    id = phoneinfo.id
    return render(request,'addborrowrecord.html',{'id':id,'borrow_mobile_name':borrow_mobile_name})

# 借出手机添加数据库
@csrf_exempt
def db_borrowphoneinfo(request,id):
    if request.POST:
        Phoneinfo.objects.filter(id=id).update(status= 1)
        borrow_person = request.POST.get('borrow_person')
        borrow_department = request.POST.get('borrow_department')
        borrow_remark = request.POST.get('borrow_remark')
        borrow_mobile_id = id
        if borrow_person is not None:
            Borrow_record_info.objects.create(
                borrow_person=borrow_person,
                borrow_department=borrow_department,
                borrow_mobile_id= borrow_mobile_id,
                borrow_remark = borrow_remark,
                )
            return HttpResponseRedirect('/successinfo/')
        else:
            return render(request, 'addborrowrecord.html', {'error': '借出人员不为空！'})

# 管理页面搜索功能
@login_required
def phonesearch(request):
    username = request.session.get('user','')
    mobile_name = request.GET.get('mobile_name','')
    phone_type = request.GET.get('phone_type', '')
    status = request.GET.get('status', '')
    system_name = request.GET.get('system_name', '')
    is_comprehensive_screen = request.GET.get('is_comprehensive_screen', '')
    is_finger_print = request.GET.get('is_finger_print', '')
    borrow_person = request.GET.get('borrow_person', '')

    search_list = dict()
    search_list['yn'] = 0
    if mobile_name:
        search_list['mobile_name'] = mobile_name
    if phone_type != '-1' :
        search_list['phone_type'] = phone_type
    if status != '-1':
        search_list['status'] = status
    if system_name:
        search_list['system_name'] = system_name
    if is_comprehensive_screen:
        search_list['is_comprehensive_screen'] = is_comprehensive_screen
    if is_finger_print:
        search_list['is_finger_print'] = is_finger_print

    phone_list = Phoneinfo.objects.filter(**search_list)
    records_count = Phoneinfo.objects.filter(**search_list).count()

    borrow_list = Borrow_record_info.objects.exclude(borrow_status=0)

    return render(request,'phoneinfo_manage.html',{'user':username,'searchphones':phone_list,'records_count':records_count,'borrowrecords':borrow_list})


def addborrowrecord(request):
    return render(request,'addborrowrecord.html')

# 借还记录
@login_required
def borrow_manage(request):
    return render(request,'borrow_manage.html')
#借出管理
@login_required
def borrow_manage(request):
    username = request.session.get('user','')
    borrow_list = Borrow_record_info.objects.exclude(borrow_status=0)
    records_count = borrow_list.count()
    return render(request,'borrow_manage.html',{'user':username,"borrowrecords":borrow_list,"records_count":records_count})

# 借出记录搜索功能
@login_required
def borrowsearch(request):
    username = request.session.get('user','')
    search_borrow_person = request.GET.get('borrow_person','')
    borrow_list = Borrow_record_info.objects.filter(borrow_person=search_borrow_person,borrow_status=1)
    records_count = borrow_list.count()
    return render(request,'borrow_manage.html',{'user':username,'borrowrecords':borrow_list,'records_count':records_count})

# 归还操作
def db_backphoneinfo(request):
    if request.POST:
        id = request.POST['id']
        print id
        Phoneinfo.objects.filter(id = id).update(status = 0)
        Borrow_record_info.objects.filter(borrow_mobile_id = id).update(borrow_status = 0)
        time = timezone.localtime(timezone.now()).strftime('%Y-%m-%d %H:%M')
        Borrow_record_info.objects.filter(borrow_mobile_id=id).update(back_time=time)
        return HttpResponse("SUCCESS")

# 用户管理
@login_required
def user_manage(request):
    username = request.session.get('user','')
    user_list = User.objects.all()
    records_count = user_list.count()
    return render(request,'user_manage.html',{'user':username,"users":user_list,"records_count":records_count})

