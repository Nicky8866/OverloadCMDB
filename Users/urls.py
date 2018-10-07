#coding:utf-8
#@Author    :   Nicky
from django.conf.urls import include, url
from Users.views import register

urlpatterns = [
        url(r'register/', register)
]