import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
import common.getCommonInfo as getCommonInfo

ware_xls = readExcel.ReadExcel().get_xls("ware.xls","ware")
url = readConfig.ReadConfig().get_http("gzhonlineurl")#获取配置文件中的url地址
ownerid = getCommonInfo.shipOwnerId

@paramunittest.parametrized(*ware_xls)
class testware(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)
    #调用测试方法
    def testware(self):
        self.recommendlist()
        self.alllist()
        self.searchlist()
        self.activewarelist()
        self.innerbuy()
        self.detail()
        self.pushdetail()
        self.innerbuydetail()
        self.recenttenorders()
        self.wareproblems()
        self.templatescontent()
        self.merchantshops()
        self.wareimagebase64()


    #获取群主可推广推荐商品列表
    def recommendlist(self):
        if self.case_name == "recommendlist":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url +"/api/ware/"+ownerid+self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #获取群主可推广所有商品列表
    def alllist(self):
        if self.case_name == "alllist":
            print(url, self.path+ownerid, self.data)
            info = RunMain().run_main(self.method, url+"/api/ware/"+ownerid+self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #获取营销活动商品列表
    def searchlist(self):
        if self.case_name == "searchlist":
            print(url, self.path+ownerid, self.data)
            info = RunMain().run_main(self.method, url+"/api/ware/"+ownerid+self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取营销活动商品列表
    def activewarelist(self):
        if self.case_name == "activewarelist":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取内购活动商品列表
    def innerbuy(self):
        if self.case_name == "innerbuy":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取商品详情
    def detail(self):
        if self.case_name == "detail":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取推送商品详情
    def pushdetail(self):
        if self.case_name == "pushdetail":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取内购商品详情
    def innerbuydetail(self):
        if self.case_name == "innerbuydetail":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取商品最近10条订单
    def recenttenorders(self):
        if self.case_name == "recenttenorders":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取商品常用问题
    def wareproblems(self):
        if self.case_name == "wareproblems":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取头部（品牌故事）、底部内容
    def templatescontent(self):
        if self.case_name == "templatescontent":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取门店
    def merchantshops(self):
        if self.case_name == "merchantshops":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #获取商品主图的base64字符串
    def wareimagebase64(self):
        if self.case_name == "wareimagebase64":
            print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])
if __name__ == '__main__':
    testware().testware()