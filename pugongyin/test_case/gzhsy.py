import json
import unittest
import paramunittest
import requests
import urllib.parse
from test_case.getOwnerid import getOwnerid
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
import common.getCommonInfo as getCommonInfo

gzhsy_xls = readExcel.ReadExcel().get_xls("gzhsy.xls","recent7dayspushcounttop3")
url = readConfig.ReadConfig().get_http("xcxbaserurl")#获取配置文件中的url地址

@paramunittest.parametrized(*gzhsy_xls)
class testgzhsy(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)
    #调用测试方法
    def testgzhsy(self):
        self.recent7dayspushcounttop3()
        self.recent7dayspushrank()
        self.recent7dayspushstatistics()
        self.indexcarousel()
        self.article()
        self.carouselarticledetail()
        self.active()
        self.testtoken()
        self.defaultshipownerinfo()
        # self.code()
        self.detail()

    #获取（公众号）营区-首页 获取七天内推广前三名
    def recent7dayspushcounttop3(self):
        if self.case_name == "recent7dayspushcounttop3":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #（公众号）营区-首页 获取七天内当前群主排名
    def recent7dayspushrank(self):
        if self.case_name == "recent7dayspushrank":
            #data = json.loads(self.data)-----
            ownerid = getOwnerid().testgetOwnerid()
            print(url, self.path+ownerid, self.data)
            info = RunMain().run_main(self.method, url + self.path+ownerid+"/recent7dayspushrank", self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #（公众号）营区-首页 当前群主最近七天推广统计
    def recent7dayspushstatistics(self):
        if self.case_name == "recent7dayspushstatistics":
            #data = json.loads(self.data)-----
            ownerid = getOwnerid().testgetOwnerid()
            print(url, self.path+ownerid, self.data)
            info = RunMain().run_main(self.method, url + self.path+ownerid+"/recent7dayspushstatistics", self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取首页轮播图
    def indexcarousel(self):
        if self.case_name == "indexcarousel":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取首页资讯
    def article(self):
        if self.case_name == "article":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取首页轮播图/资讯详细内容
    def carouselarticledetail(self):
        if self.case_name == "carouselarticledetail":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#获取首页营销活动和内购
    def active(self):
        if self.case_name == "active":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#获取测试token
    def testtoken(self):
        if self.case_name == "testtoken":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])
#获取默认群主信息
    def defaultshipownerinfo(self):
        if self.case_name == "defaultshipownerinfo":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#获取绑定验证码
    def code(self):
        if self.case_name == "code":
            #data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 获取登录信息
    def detail(self):
        if self.case_name == "detail":
            # data = json.loads(self.data)-----
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])
if __name__ == '__main__':
    testgzhsy().testgzhsy()