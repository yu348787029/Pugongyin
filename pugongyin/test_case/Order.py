#author：zwx
import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig

order_xls = readExcel.ReadExcel().get_xls("login.xls","order")
url = readConfig.ReadConfig().get_http("xcxbaserurl")#获取配置文件中的url地址

@paramunittest.parametrized(*order_xls)
class testUserOrder(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)

    #调用测试方法
    def testuserOrder(self):
        self.OrderCheckResult()
        self.orderclose()
        self.innerbuyorder()

    '''正常下单流程参数解释
        "PushlogId": "c450a7ac-000e-4815-8c78-368cd7660269", 推广人id
    	"WareId": "3d1bde5b-2ccd-477e-8fef-36f21e55b341",商品id
    	"WareSkuId": "SM00219070185",商品sku
    	"WareNum": 1,
    	"OrderSourceType": 4,
    	"DeliverType": 2,
    	下单人手机以及地址
    	"UserName": "",TelNumber": "","PostalCode": "","ProvinceName": "","CityName": "","CountyName": "","DetailInfo": "",
    	"CouponCode": "",优惠券
    	"token": "", token
    	固定参数不变
    	"AppInfoCode": "code001","MerchantId": "645d5071-1c22-4161-a093-7566f5cca058"
            '''
    #正常下单流程
    def OrderCheckResult(self):
        if self.case_name == "userorder":
            data = json.loads(self.data)
            #print(url+self.path,data)
            info = RunMain().run_main(self.method,url+self.path,data)
            res = json.loads(info)
            self.assertEqual(res['Code'],"000000")
            self.assertFalse(res['IsError'])
            print("此订单的订单号为：",res['Data'])
            global ordersno
            ordersno=res['Data']

    #用户取消订单
    def orderclose(self):
        if self.case_name == "userorderclose":
            data = json.loads(self.data)
            #print(url+self.path+ordersno, data)
            info = RunMain().run_main(self.method, url + self.path+ordersno, data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])
            self.assertEqual(res['Data'], "true")

    #内购下单流程
    def innerbuyorder(self):
        if self.case_name == "innerbuyorder":
            data = json.loads(self.data)
            #print(url+self.path,data)
            info = RunMain().run_main(self.method,url+self.path,data)
            res = json.loads(info)
            self.assertEqual(res['Code'],"000000")
            self.assertFalse(res['IsError'])
            print("此内购订单的订单号为：",res['Data'])



if __name__ == '__main__':
    testUserOrder().testuserOrder()