#coding:utf-8
#@Author    :   Nicky
import os
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from Users.forms import CMDBUserForm
from Service.models import CMDBUser
from XueGodCMDB.settings import BASE_DIR
from django.http import HttpResponse
from django.db import connection


def loginValid(func):
    def valid(request, *args, **keywords):
        username = request.COOKIES.get("username")
        if username:
            try:
                user = CMDBUser.objects.get(username=username)
            except:
                return HttpResponseRedirect('/login/', locals())
            else:
                return func(request)
        else:
            return HttpResponseRedirect('/login/', locals())
    return valid

@loginValid
def index(request):
    forms = CMDBUserForm()
    if request.method == "POST" and request.POST and request.FILES:
        formsData = CMDBUserForm(data=request.POST, files=request.FILES)
        if formsData.is_valid():
            requestData = formsData.cleaned_data
            username = requestData.get('username')
            password = requestData.get('password')
            nickname = requestData.get('nickname')
            phone = requestData.get('phone')
            email = requestData.get('email')
            photo = requestData.get('photo').name

            #实例化数据库，保存数据
            user = CMDBUser()
            user.username = username
            user.password = password
            user.nickname = nickname
            user.phone = phone
            user.email = email
            user.photo = photo
            user.save()

            #保存文件，没有限制文件格式
            photofile = request.FILES.get('photo')
            path = os.path.join(BASE_DIR, 'static\\images\\%s' % photofile.name)
            with open(path, 'wb') as f:
                for chunk in photofile.chunks():
                    f.write(chunk)

        else:
            print(formsData.errors)

    return render(request, 'index.html', locals())

def echart(request):
    return render_to_response("echart.html")

def login(request):
    if request.method == "POST" and request.POST:
    #获取校验cookie
        login_cookie = request.get_signed_cookie(key='login_cookie', salt='小霸王')
        if login_cookie:
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            try:
                user = CMDBUser.objects.get(username=username)
            except:
                return HttpResponse('用户名不存在，请确认后重新输入。')
            else:
                db_password = user.password
                if password == db_password:
                    response = HttpResponseRedirect('/index/', locals())
                    response.set_cookie(key='username', value=user.username)
                    return response
                else:
                    return HttpResponse('密码错误！')
        else:
            return HttpResponse("404")

    else:
        #生成response实例
        response = render(request, 'login.html')
        #设置cookie
        response.set_signed_cookie('login_cookie', 'helloworld', salt='小霸王',max_age=3600)
        return response

def getPage(sql,page,num=10):
    """
    后端分页函数
    :param sql: 查询语句
    :param page: 当前页码
    :param num: 单页显示条数
    :return:
    """
    page = int(page)
    num = int(num)
    start_page = (page - 1) * num
    page_sql = sql + " limit %s,%s"% (start_page, num)
    cursor = connection.cursor()
    cursor.execute(page_sql)
    page_data = cursor.fetchall()
    keys = [key[0] for key in cursor.description]
    result = [dict(zip(keys, d)) for d in page_data]
    return {"page_data": result}

def vueExample(request):
    return render(request, "vueExample.html")

def gate(request):
    return render(request, "gateoneExample.html")

