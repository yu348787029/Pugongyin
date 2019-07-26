import requests
import json
#from common.Log import MyLog as Log
session = requests.Session()
#-------------主方法请求类 get post 等传参返回结果--------------
class RunMain():
    def send_Post(self, url, data):
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_Get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post' or method == 'POST':
            result = self.send_Post(url, data)
        elif method == 'get' or method == 'GET':
            result = self.send_Get(url, data)
        else:
            print("method值错误")
        return result
