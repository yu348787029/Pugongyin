import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
import common.getCommonInfo as getCommonInfo

showcase_xls = readExcel.ReadExcel().get_xls("gzh_showcase.xls","showcase")
url = readConfig.ReadConfig().get_http("gzhonlineurl")#获取配置文件中的url地址
shipOwnerId = getCommonInfo.shipOwnerId
wareId = getCommonInfo.getWareId()
xcxtoken = getCommonInfo.getXcxToken()


@paramunittest.parametrized(*showcase_xls)
class testgzxcxcase(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)
    #调用测试方法
    def testgzxcxcase(self):
        # self.getAccountInfo()
        # self.getBuyrecord()
        # self.getFavoriteware()
        # self.getCanclefavoriteware()
        # self.getClickrecord()
        # self.getCreditscalculaterecord()
        # self.getCreditsrecord()
        # self.getCurrentordercredits()
        # self.getCurrentpushwares()
        # self.getCurrentsearchordercredits()
        # self.getEarninginfo()
        # self.getPrevordercredits()
        # self.getPrevpushwares()
        # self.getPrevsearchordercredits()
        # self.getPushrecord()
        # self.getMemberaccountinfo()
        # self.xcx_order()
        # self.getOrderdetail()
        # self.getOrderlogistics()
        self.getWithdrawlog()

    #获取（公众号）营区-首页 获取七天内推广前三名
    def getAccountInfo(self):
        if self.case_name == "getAccountInfo":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/accountinfo', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #公众号--获取推广记录的成交记录
    def getBuyrecord(self):
        if self.case_name == "getBuyrecord":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/1/10' + '/buyrecord', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #群主取消收藏商品
    def getCanclefavoriteware(self):
        if self.case_name == "getCanclefavoriteware":
            data = json.loads(self.data)
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/' + wareId + '/canclefavoriteware',data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #公众号--获取推广记录的点击记录
    def getClickrecord(self):
        if self.case_name == "getClickrecord":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/1/10' + '/clickrecord', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #公众号--获取三个月内已结算积分记录
    def getCreditscalculaterecord(self):
        if self.case_name == "getCreditscalculaterecord":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/creditscalculaterecord', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)

            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

   #公众号--获取积分记录（待入账、已入账）
    def getCreditsrecord(self):
        if self.case_name == "getCreditsrecord":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/2' + '/creditsrecord', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#本月订单积分
    def getCurrentordercredits(self):
        if self.case_name == "getCurrentordercredits":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/2' + '/currentordercredits', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#本月推送商品
    def getCurrentpushwares(self):
        if self.case_name == "getCurrentpushwares":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/currentpushwares', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#本月订单积分查询
    def getCurrentsearchordercredits(self):
        if self.case_name == "getCurrentsearchordercredits":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/currentsearchordercredits', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

#公众号-- 获取群主收益信息
    def getEarninginfo(self):
        if self.case_name == "getEarninginfo":
            data = json.loads(self.data)
            print(data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + '?token=gzhlogin:0f289302-3cbd-4a5a-8e47-edd071a0a1d0', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 收藏商品
    def getFavoriteware(self):
        if self.case_name == "getFavoriteware":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/' + wareId + '/favoriteware', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 上月订单积分
    def getPrevordercredits(self):
        if self.case_name == "getPrevordercredits":
            print("---------99------- ")
            print(self.data)
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/2' + '/prevordercredits', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 上月推送商品
    def getPrevpushwares(self):
        if self.case_name == "getPrevpushwares":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/prevpushwares', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 上月订单积分查询
    def getPrevsearchordercredits(self):
        if self.case_name == "getPrevsearchordercredits":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/prevsearchordercredits', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 公众号--获取推广记录
    def getPushrecord(self):
        if self.case_name == "getPushrecord":
            data = json.loads(self.data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/1/10' + '/pushrecord', data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 微信小程序-- 获取用户账号信息
    def getMemberaccountinfo(self):
        if self.case_name == "getMemberaccountinfo":
            data = json.loads(self.data)
            print(data)
            # 调用 configHTTP 类中的run_main方法
            info = RunMain().run_main(self.method, url + self.path + 'memberaccountinfo?token=' + xcxtoken, data)
            # 将得到的返回值进行格式化并取值判断
            res = json.loads(info)
            print(res)
            if self.case_name == "getMemberaccountinfo":
                self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

# 小程序订单
    def xcx_order(self):
        data = json.loads(self.data)
        if self.case_name == "getOrder":
            info = RunMain().run_main(self.method,
                                      url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&status=&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",
                                      data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            print("-----全部订单------")

        if self.case_name == "getReadyPayOrder":
            info = RunMain().run_main(self.method,
                                      url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&status=1&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",
                                      data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            print("-----待付款订单------")

        if self.case_name == "getReadySendOrder":
            info = RunMain().run_main(self.method,
                                      url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&status=2&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",
                                      data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            print("-----待发货订单------")

# 小程序订单详情
    def getOrderdetail(self):
        if self.case_name == "getOrderdetail":
            data = json.loads(self.data)
            info = RunMain().run_main(self.method,
                                      url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&ordersn=po201908011324597581805&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",
                                      data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            print("-----订单详情------")
            self.assertFalse(res['IsError'])

# 订单物流信息
    def getOrderlogistics(self):
        if self.case_name == "getOrderlogistics":
            data = json.loads(self.data)
            info = RunMain().run_main(self.method,
                                      url + self.path + "/po201908011324597581805/orderlogistics?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",
                                      data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            print("-----物流信息------")
            self.assertFalse(res['IsError'])


# 提现记录
    def getWithdrawlog(self):
        if self.case_name == "getWithdrawlog":
            data = json.loads(self.data)
            info = RunMain().run_main(self.method,url + self.path ,data)
            res = json.loads(info)
            print(res)
            self.assertEqual(res['Code'], "000000")
            print("-----提现记录------")
            self.assertFalse(res['IsError'])




if __name__ == '__main__':
    testgzxcxcase().testgzxcxcase()