"""equipments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from phoneinfo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login),
    url(r'^logout/', views.logout),
    url(r'^home/', views.home),
    url(r'^left/', views.left),
    url(r'^top/', views.top),
    url(r'^add/phoneinfo/', views.addphoneinfo),
    url(r'^add/borrowrecord/', views.addborrowrecord),
    url(r'^show/phoneinfo/([1-9][0-9]*)/', views.show_changephoneinfo),
    url(r'^change/phoneinfo/([1-9][0-9]*)/', views.db_changephoneinfo),
    url(r'^delete/phoneinfo/', views.db_deletephoneinfo),
    url(r'^back/phoneinfo/', views.db_backphoneinfo),
    url(r'^show/borrowphone/([1-9][0-9]*)/', views.show_borrowphoneinfo),
    url(r'^borrow/phoneinfo/([1-9][0-9]*)/', views.db_borrowphoneinfo),
    url(r'^phoneinfo_manage/', views.phoneinfo_manage),
    url(r'^borrow_manage/', views.borrow_manage),
    url(r'^db_addphoneinfo/', views.db_addphoneinfo),
    url(r'^phonesearch/', views.phonesearch),
    url(r'^borrow_mobile/', views.borrow_manage),
    url(r'^borrowsearch/', views.borrowsearch),
    url(r'^successinfo/', views.successinfo),
    # url(r'^user_manage/', views.user_manage),
]
