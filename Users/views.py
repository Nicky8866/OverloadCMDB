from django.shortcuts import render
from django.http import JsonResponse
from Users.forms import CMDBUserForm
from Service.models import CMDBUser
from XueGodCMDB.settings import BASE_DIR
import os

# Create your views here.

def register(request):
    result = {"submit": "success"}
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
            return JsonResponse(result)
        else:
            print(formsData.errors)
            result["submit"] = "error"
            return JsonResponse(result)
    else:
        return JsonResponse({"method": "GET"})