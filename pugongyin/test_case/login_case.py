import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig

login_xls = readExcel.ReadExcel().get_xls("login.xls","login")
url = readConfig.ReadConfig().get_http("baseurl")#获取配置文件中的url地址



#@paramunittest.parametrized(*变量名)-----变量名为excel文件，
#setParameters方法里面的参数为excel文件中的列的变量名，必须与之完全一样，不能多加和少减
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "------------测试开始------------------")

    #调用测试方法
    def testLogin(self):
        self.checkResult()
    def tearDown(self):
        print(self.case_name + "------------测试结束------------------\n\n")

    def checkResult(self):
        #将读取到的 data 转为 json格式
        data = json.loads(self.data)
        #调用 configHTTP 类中的run_main方法
        print(url,self.path,data)
        info = RunMain().run_main(self.method,url+self.path,data)
        #将得到的返回值进行格式化并取值判断
        print("fanhuizhi:",info)
        res = json.loads(info)
        print("zhuagtaima",res['Code'])
        if self.case_name == "login":
            self.assertEqual(res['Code'],"0000")
            self.assertTrue(res['IsSuccess'])
            self.assertEqual(res['Message'], "登录成功")
        if self.case_name == "login_errorpwd":
            self.assertEqual(res['Code'], '0001')
            self.assertFalse(res['IsSuccess'])
            self.assertEqual(res['Message'], "用户名或密码错误")
        if self.case_name == "login_notuser":
            self.assertEqual(res['Code'], '0001')
            self.assertFalse(res['IsSuccess'])
            self.assertEqual(res['Message'], "用户名或密码错误")

if __name__ == '__main__':
    testUserLogin.testLogin()