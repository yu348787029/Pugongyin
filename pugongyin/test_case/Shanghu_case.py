import json
import unittest
import paramunittest
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig

login_xls = readExcel.ReadExcel().get_xls("login.xls","shagnhu")
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
    def testShanghu(self):
        self.checkResult()

    def tearDown(self):
        print(self.case_name +"---------------测试结束------------\n\n")

    def checkResult(self):
        #将读取到的 data 转为 json格式
        data = json.loads(self.data)
        #调用 configHTTP 类中的run_main方法
        cookie_headers = {
            #"Cookie": ".ASPXAUTH=4D491D7BFF7D5A13AD34BB529DFD5F7E7257687FBC92B273C73CE6C1FA6C36385CC6805A5F8660E407FDD47F854B6DAAC131E1C7F913CB2C22DF3BBBB120F2F3FE5485AE7897AED413AA186D70B0F3F0B39BB60D54DB04B8F89657BDA0528DD71F70D634070636225C358C006152FB62AA950767B8916C60402EA7FD7ED58A501DA556D0E62CB96FBF2DCDFDFBAAEA418598D4C9056E050A3E7237351841C67E"
        }
        info = RunMain().run_main(self.method,url+self.path,data)
        #将得到的返回值进行格式化并取值判断
        print("fanhuizhi:",info)
        res = json.loads(info)
        print("zhuagtaima",res['code'])
        if self.case_name == "shagnhu":
            self.assertEqual(res['code'],0)


if __name__ == '__main__':
    testUserLogin.testShanghu()