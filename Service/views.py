from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from Service.models import Service
from django.core.paginator import Paginator
from XueGodCMDB.views import getPage


# Create your views here.

def server(request,page=1):
    #查询所有数据
    servers = Service.objects.all()
    #进行分页
    p_servers = Paginator(servers, 10)
    pageData = p_servers.page(page)
    #此处不使用locals()返回前端是为了避免注入导致数据泄露，所以指定值返回
    return render(request, "ServerList.html", {"pageData": pageData, "pageRange": p_servers.page_range})

def AjaxService(request,page=1):
    sql = "select * from Service_service"
    page_data = getPage(sql=sql, page=page)
    page_range = [1,2,3,4,5,6,7,8,9,10]
    page_data["page_range"] = page_range
    return JsonResponse(page_data)

def ServerList_ajax(request):
    return render(request, "ServerList_ajax.html")

def getConnect(request):
    if request.method == "GET" and request.GET:
        id = int(request.GET.get("id"))
        server = Service.objects.get(id=id)
        return render(request, "getConnect.html")
    else:
        return HttpResponse("Your method must be get!")

#完成gateone请求的验证url和验证信息的计算生成
import time,hmac,hashlib,json


def authodj(secret, **parts):
    """
            对secret值安装gateone的要求加密
        """
    hash = hmac.new(secret, digestmod=hashlib.sha1)
    for parts in parts:
        hash.update(str(parts))
    return hash.hexdigest()

def gateValid(request):
    user = "root"
    gateone_server = "https://10.66.3.131" #后期代码整理，我们可以放到settings当中

    api_key = "MjhmYzA1YjAwMjNjNDgyNGJiYWY5NmE5MzcyNWFlNjYyY"
    secret = "YjNiMjA5YTBmNmFmNDBhMmE2YTEyNDVmYWM0NWRkOGVlZ".encode()


    authodj_dict = {
        'api_key': api_key,
        'upn': 'gateone',
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(secret,digestmod=hashlib.sha1)
    update_data = authodj_dict['api_key'] + authodj_dict['upn'] + authodj_dict['timestamp']
    my_hash.update(update_data.encode())

    authodj_dict['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url": gateone_server, "auth": authodj_dict}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    return HttpResponse(valid_json_auth_info)
