#coding:utf-8
#@Author    :   Nicky
from django.conf.urls import include, url
from Api.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
        url(r'CMDBApi/', csrf_exempt(CMDBApi.as_view()))
]