#coding:utf-8
#@Author    :   Nicky

from django.shortcuts import render_to_response
from Users.forms import CMDBUserForm


def index(request):
    forms = CMDBUserForm()
    return render_to_response('index.html', locals())
