import requests
import time, hashlib

APPID = 'lgxy@smc_host_api'				# 和服务器端一样的id

def md5(appid):
    new_time = str(time.time())
    m = hashlib.md5()
    m.update(bytes(appid + new_time,encoding='utf-8'))
    return m.hexdigest(),new_time

data, client_time = md5(APPID)

new_appid = "%s|%s" %(data, client_time)
# new_appid = 'a94ff928a82749d017a873902922e650|1501150616.916467'

print(new_appid)
# 各种请求的发送
# a = requests.get(url='http://127.0.0.1:8000/',
#                  headers={'appid':new_appid })
#
# a = requests.delete(url='http://127.0.0.1:8000/index/',
#                     	={'name':'sunyang'})

a = requests.get(url='http://127.0.0.1:8888/api/host_api/',
                    params={'name':'haha'},headers={'appid':new_appid })
# print(a.json())
print(a.text)
