import json
import unittest
import paramunittest
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig

login_xls = readExcel.ReadExcel().get_xls("gzh.xls","gzhlogin")#引入excel用例文档中需要的
url = readConfig.ReadConfig().get_http("gzhbaseurl")#获取配置文件中的url地址


#@paramunittest.parametrized(*变量名)-----变量名为excel文件，
#setParameters方法里面的参数为excel文件中的列的变量名，必须与之完全一样，不能多加和少减
@paramunittest.parametrized(*login_xls)
class testT(unittest.TestCase):

    '''def _init_(self):
        global ShipOwnerId
        ShipOwnerId = {}
    def set_value(key, value):
        """ 定义一个全局变量 """
        ShipOwnerId[key] = value

    def get_value(key, defValue=None):
        #""" 获得一个全局变量,不存在则返回默认值 """
        try:
            return ShipOwnerId[key]
        except KeyError:
            return defValue
    def settest(self):
        testT.set_value('ShipOwnerId', ShipOwnerId)'''

    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)


    def test(self):
        print("---------------- ")

        i = ""
        #将读取到的 data 转为 json格式
        data = json.loads(self.data)
        #调用 configHTTP 类中的run_main方法
        info = RunMain().run_main(self.method,url+self.path,data)
        #将得到的返回值进行格式化并取值判断
        res = json.loads(info)
        if self.case_name == "gzhlogincase":
            self.assertEqual(res['Code'],"000000")
            self.assertFalse(res['IsError'])
            global ShipOwnerId
            ShipOwnerId = res['Data']['ShipOwnerId']
        if self.case_name == "login_errorpwd":
            self.assertEqual(res['Code'], '400000')
            self.assertFalse(res['IsError'])
            self.assertEqual(res['Msg'], "用户登录已过期")
        print("方法内："+ShipOwnerId)
        print(type(ShipOwnerId))
        return ShipOwnerId

    def test1(self):
        print("aaaaaaaaaaa",ShipOwnerId)


if __name__== "__main__":
    testT.test1()
    testT.get_value('ShipOwnerId')
    print(testT.get_vlue('ShipOwnerId'))
    #ShipOwnerId = testT().test()