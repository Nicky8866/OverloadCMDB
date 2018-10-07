#coding:utf-8
#@Author    :   Nicky
import json
from urllib import parse, request


url = "http://127.0.0.1:8000/api/CMDBApi/"
user_pasw = {
    "username": "nicky",
    "password": "123456"
}
json_data = json.dumps(user_pasw)

data = {
    "type": "login",
    "data": json_data,
    "token": ""
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

sendData = parse.urlencode(data).encode()
req = request.Request(url=url, headers=headers, data=sendData)
response = request.urlopen(req)
result = response.read().decode()
print(result)