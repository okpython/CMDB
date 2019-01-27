# 采集数据
import subprocess
import requests

result = subprocess.getouput("ipconfig")
# result正则处理获取想要的数据
data_dict = {
    'nic':{},
    'disk':{},
    'mem':{}
}

# 发送数据
requests.post("http://127.0.0.1:8000/assets.html", data=data_dict)

















