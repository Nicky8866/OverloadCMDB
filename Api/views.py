from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from Service.models import CMDBUser
from Api.models import Token
import random
import datetime
from Service.models import Cpu,Memory,Service,Service_Cpu,Service_Memory
# Create your views here.


def getToken(user_id):
    """
        根据用户id生成token
        token生成规则：随机数10位
    """
    temp = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = random.sample(temp, 10)
    value = "".join(value)
    t = Token()
    t.value = value
    t.time = 3600 #单位是秒
    t.create_time = datetime.datetime.now()
    t.user_id = user_id
    t.save()
    return value


class CMDBApi(View):
    """
        接口包含两个post功能：
        1、登录
        2、cpu信息收集
    """
    def __init__(self, **kwargs):
        #View.__init__(self, **kwargs)
        super(View, self).__init__(**kwargs)
        self.result = {
            "status": "error",
            "data": {},
            "error": ""
        }
        #过滤dir(self)当中所有以“api_”开头的方法
        self.item = list(
            filter(lambda x: x.startswith("api_"), dir(self)))
        # 获取该类所有的方法名称和方法本身
        self.dict = CMDBApi.__dict__

    def api_login(self):
        username = self.postData.get("username")
        password = self.postData.get("password")
        #进行密码校验
        if username:
            try:
                user = CMDBUser.objects.get(username=username)
            except Exception as e:
                self.result["error"] = "The user:%s is not exist" % username
                print(e)
            else:
                db_password = user.password
                if password == db_password:
                    # token valid 可以在这里校验当前id是否已有对应的未过期token
                    # 使用当前时间戳-创建的时间戳
                    # 如果差小于3600代表可以
                    # 如果大于代表过期
                    # 如果小于0代表非法
                    user_id = user.id
                    token = getToken(user_id)
                    self.result["status"] = "success"
                    self.result["data"] = {"token": token}
                else:
                    self.result["error"] = "your password is incorrect"

    def api_sendServer(self):
        #获取客户端提交的数据
        post_server = json.loads(self.postData["server"])
        post_cpu = json.loads(self.postData["cpu"])
        post_memory = json.loads(self.postData["memory"])

        #保存服务器信息
        server = Service()
        server.hostname = post_server.get("hostname")
        server.ip = post_server.get("ip")
        server.mac = post_server.get("mac")
        server.cpu = post_server.get("cpu")
        server.memory = post_server.get("memory")
        server.isalive = 'true'
        server.save()

        #保存cpu信息
        cpu = Cpu()
        cpu.processor = post_cpu.get("processor")
        cpu.vendor_id = post_cpu.get("vendor_id")
        cpu.cpu_family = post_cpu.get("cpu_family")
        cpu.model = post_cpu.get("model")
        cpu.model_name = post_cpu.get("model_name")
        cpu.stepping = post_cpu.get("stepping")
        cpu.microcode = post_cpu.get("microcode")
        cpu.cpu_MHz = post_cpu.get("cpu_MHz")
        cpu.cache_size = post_cpu.get("cache_size")
        cpu.physical_id = post_cpu.get("physical_id")
        cpu.siblings = post_cpu.get("siblings")
        cpu.core_id = post_cpu.get("core_id")
        cpu.cpu_cores = post_cpu.get("cpu_cores")
        cpu.apicid = post_cpu.get("apicid")
        cpu.initial_apicid = post_cpu.get("initial_apicid")
        cpu.fpu = post_cpu.get("fpu")
        cpu.fpu_exception = post_cpu.get("fpu_exception")
        cpu.cpuid_level = post_cpu.get("cpuid_level")
        cpu.wp = post_cpu.get("wp")
        cpu.flags = post_cpu.get("flags")
        cpu.bogomips = post_cpu.get("bogomips")
        cpu.clflush_size = post_cpu.get("clflush_size")
        cpu.cache_alignment = post_cpu.get("cache_alignment")
        cpu.address_sizes = post_cpu.get("address_sizes")
        cpu.power_management = post_cpu.get("power_management")
        cpu.save()

        #保存内存信息
        memory = Memory()
        memory.MemTota = post_memory.get("MemTota")
        memory.MemFree = post_memory.get("MemFree")
        memory.MemAvailable = post_memory.get("MemAvailable")
        memory.Buffers = post_memory.get("Buffers")
        memory.Cached = post_memory.get("Cached")
        memory.SwapCached = post_memory.get("SwapCached")
        memory.Active = post_memory.get("Active")
        memory.Inactive = post_memory.get("Inactive")
        memory.Active_anon = post_memory.get("Active_anon")
        memory.Inactive_anon = post_memory.get("Inactive_anon")
        memory.Active_file = post_memory.get("Active_file")
        memory.Inactive_file = post_memory.get("Inactive_file")
        memory.Unevictable = post_memory.get("Unevictable")
        memory.Mlocked = post_memory.get("Mlocked")
        memory.SwapTotal = post_memory.get("SwapTotal")
        memory.SwapFree = post_memory.get("SwapFree")
        memory.Dirty = post_memory.get("Dirty")
        memory.Writeback = post_memory.get("Writeback")
        memory.AnonPages = post_memory.get("AnonPages")
        memory.Mapped = post_memory.get("Mapped")
        memory.Shmem = post_memory.get("Shmem")
        memory.Slab = post_memory.get("Slab")
        memory.SReclaimable = post_memory.get("SReclaimable")
        memory.SUnreclaim = post_memory.get("SUnreclaim")
        memory.KernelStack = post_memory.get("KernelStack")
        memory.PageTables = post_memory.get("PageTables")
        memory.NFS_Unstable = post_memory.get("NFS_Unstable")
        memory.Bounce = post_memory.get("Bounce")
        memory.WritebackTmp = post_memory.get("WritebackTmp")
        memory.CommitLimit = post_memory.get("CommitLimit")
        memory.Committed_AS = post_memory.get("Committed_AS")
        memory.VmallocTotal = post_memory.get("VmallocTotal")
        memory.VmallocUsed = post_memory.get("VmallocUsed")
        memory.VmallocChunk = post_memory.get("VmallocChunk")
        memory.HardwareCorrupted = post_memory.get("HardwareCorrupted")
        memory.AnonHugePages = post_memory.get("AnonHugePages")
        memory.HugePages_Total = post_memory.get("HugePages_Total")
        memory.HugePages_Free = post_memory.get("HugePages_Free")
        memory.HugePages_Rsvd = post_memory.get("HugePages_Rsvd")
        memory.HugePages_Surp = post_memory.get("HugePages_Surp")
        memory.Hugepagesize = post_memory.get("Hugepagesize")
        memory.DirectMap4k = post_memory.get("DirectMap4k")
        memory.DirectMap2M = post_memory.get("DirectMap2M")
        memory.DirectMap1G = post_memory.get("DirectMap1G")
        memory.save()

        #保存Server_CPU的对应关系
        s_c = Service_Cpu()
        s_c.service_id = server.id
        s_c.cpu_id = cpu.id
        s_c.save()

        #保存Server_内存的对应关系
        s_m = Service_Memory()
        s_m.service_id = server.id
        s_m.memory_id = memory.id
        s_m.save()

        #返回信息
        self.result["status"] = "success"
        self.result["data"] = "save server is success"

    def get(self, request):
        # self.result["error"] = "we have no method named get"
        # return JsonResponse(self.result)
        # item = self.__dict__ #由于是web请求异步的原因，self的dict当中查找不到api系列方法
        item = self.dict
        return render(request, "get_page.html", locals())

    def post(self, request):
        """
            如果是post并且post有值
            我们判定是login还是sendServer
        :return:
        """
        if request.method == "POST" and request.POST:
            data = request.POST
            ty = data.get("type")
            dt = data.get("data")
            tk = data.get("token")
            self.postData = json.loads(dt.replace("\'", "\""))
            # 如果有类型值，判断是否有指定类型接口
            ty_name = "api_" + ty
            # 判断类型是否存在，并且属于已有的类型
            if ty and ty_name in self.item:
                # 获取当前类的所有以api开头的方法
                try:
                    self.dict[ty_name](self)
                except Exception as e:
                    print(e)
            else:
                self.result["error"] = "we have no method named %s." % ty
        return JsonResponse(self.result)





"""
def getServer(by, ip):
    pass

@csrf_exempt
def CMDBApi(request):
    #定义响应的结构
    result = {
        "status": "error",
        "data": {},
        "error": "",
    }
    if request.method == "POST" and request.POST:
        data = request.POST
        ty = data.get("type")
        dt = data.get("data")
        tk = data.get("token")
        if ty and dt and tk:
            if ty == "getServer":
                pass
            else:
                result["error"] = "The method [%s] is not exist" % ty
        elif tk == "" and ty == "login" and dt:
            dt = json.loads(dt)
            username = dt.get("username")
            password = dt.get("password")
            token = login(username, password)["token"]
            if token:
                result["status"] = "success"
                result["data"] = {"token": token}
            else:
                result["error"] = login(username, password)["error"]
        else:
            result["error"] = "data is not true"
    else:
        result["error"] = "request must be POST and data not be NULL"
    return JsonResponse(result)
"""