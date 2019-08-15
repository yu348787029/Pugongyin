import json
import unittest
import paramunittest
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
import common.getCommonInfo as getCommonInfo

gzh_accountInfo = readExcel.ReadExcel().get_xls("gzh_showcase.xls", "order")  # 引入excel用例文档中需要的
url = readConfig.ReadConfig().get_http("gzhonlineurl")  # 获取配置文件中的url地址
shipOwnerId = getCommonInfo.shipOwnerId
xcxtoken = getCommonInfo.getXcxToken()


# @paramunittest.parametrized(*变量名)-----变量名为excel文件，
# setParameters方法里面的参数为excel文件中的列的变量名，必须与之完全一样，不能多加和少减
@paramunittest.parametrized(*gzh_accountInfo)
class testT(unittest.TestCase):

    def setParameters(self, case_name, path, data, method, isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)

    def test(self):
        data = json.loads(self.data)
        if self.case_name == "getOrder":
            info = RunMain().run_main(self.method,url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&status=&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            print("-----全部订单------")

        if self.case_name == "getReadyPayOrder":
            info = RunMain().run_main(self.method,url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&status=1&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            print("-----待付款订单------")

        if self.case_name == "getReadySendOrder":
            info = RunMain().run_main(self.method,url + self.path + "?token=xcxlogin%3A16e265ff-ff1f-4ab1-a998-1f6325c8a357&status=2&AppInfoCode=code001&MerchantId=645d5071-1c22-4161-a093-7566f5cca058",data)
            res = json.loads(info)
            self.assertEqual(res['Code'], "000000")
            print("-----待发货订单------")



if __name__ == "__main__":
    testT.test()

