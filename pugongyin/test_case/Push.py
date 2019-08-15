#author：zwx
import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig

push_xls = readExcel.ReadExcel().get_xls("login.xls","push")
url = readConfig.ReadConfig().get_http("xcxbaserurl")#获取配置文件中的url地址

@paramunittest.parametrized(*push_xls)
class testpush(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)

    #调用测试方法
    def testuserOrder(self):
        self.pushlog()
        self.shareposter()

    #添加推送记录
    def pushlog(self):
        if self.case_name == "pushlog":
            data = json.loads(self.data)
            print(url+self.path,data)
            info = RunMain().run_main(self.method,url+self.path,data)
            res = json.loads(info)
            self.assertEqual(res['Code'],"000000")
            self.assertFalse(res['IsError'])

    #GET /api/push/shareposter获取公众号商品分享海报
    def shareposter(self):
        if self.case_name == "shareposter":
            data = json.loads(self.data)
            print(url+self.path,data)
            info = RunMain().run_main(self.method,url+self.path,data)
            res = json.loads(info)
            self.assertEqual(res['Code'],"000000")
            self.assertFalse(res['IsError'])

    #添加群主默认的推广记录（默认群主与随机商品）和访问记录，小程序外链进入蒲公英小程序专用/api/push/adddefaultpushlog
    def adddefaultpushlog(self):
        if self.case_name == "adddefaultpushlog":
            data = json.loads(self.data)
            print(url+self.path,data)
            info = RunMain().run_main(self.method,url+self.path,data)
            res = json.loads(info)
            self.assertEqual(res['Code'],"000000")
            self.assertFalse(res['IsError'])

if __name__ == '__main__':
    testpush().testpush()