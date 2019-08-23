import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
#from test_case.A import testT
'''
ownerid_xls = readExcel.ReadExcel().get_xls("login.xls","ownerid")
url = readConfig.ReadConfig().get_http("xcxbaserurl")#获取配置文件中的url地址

@paramunittest.parametrized(*ownerid_xls)'''
#获取当前登陆的Ownerid
class getOwnerid(unittest.TestCase):
    '''
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)'''
    '''
    #获取ownerid
    def testgetOwnerid11(self):
    #if self.case_name == "gzhlogincase":
        self.method = readConfig.ReadConfig().get_http("method")
        self.path = readConfig.ReadConfig().get_http("path")
        self.data = readConfig.ReadConfig().get_http("data")
        self.url = readConfig.ReadConfig().get_http("gzhbaseurl")

        data = json.loads(self.data)
        # 调用 configHTTP 类中的run_main方法

        info = RunMain().run_main(self.method, self.url + self.path, data)
        # 将得到的返回值进行格式化并取值判断
        res = json.loads(info)
        self.assertEqual(res['Code'], "000000")
        self.assertFalse(res['IsError'])
        global ShipOwnerId
        ShipOwnerId = res['Data']['ShipOwnerId']
        print("方法内：" + ShipOwnerId)
        print(type(ShipOwnerId))
        return ShipOwnerId'''

    def testgetOwnerid(self):
        # if self.case_name == "gzhlogincase":
        method = readConfig.ReadConfig().get_http("method")
        path = readConfig.ReadConfig().get_http("path")
        data = readConfig.ReadConfig().get_http("data")
        url = readConfig.ReadConfig().get_http("gzhbaseurl")

        datajson = json.loads(data)
        print(datajson)
        print(url + path )
        info = RunMain().run_main(method, url + path, datajson)
        res = json.loads(info)
        print("----",res)
        if res['Code']=="000000":
            global ShipOwnerId
            ShipOwnerId = res['Data']['ShipOwnerId']
        else:
            print("ShipOwnerId值错误")
        return ShipOwnerId

if __name__ == '__main__':
    getOwnerid().testgetOwnerid()