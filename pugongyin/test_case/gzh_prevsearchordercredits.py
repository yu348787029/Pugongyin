import json
import unittest
import paramunittest
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
import common.getCommonInfo as getCommonInfo

gzh_accountInfo = readExcel.ReadExcel().get_xls("gzh_showcase.xls", "prevsearchordercredits")  # 引入excel用例文档中需要的
url = readConfig.ReadConfig().get_http("gzhonlineurl")  # 获取配置文件中的url地址
shipOwnerId = getCommonInfo.shipOwnerId


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
        print("---------99------- ")
        print(self.data)
        data = json.loads(self.data)
        # 调用 configHTTP 类中的run_main方法
        info = RunMain().run_main(self.method, url + self.path + shipOwnerId + '/prevsearchordercredits', data)
        # 将得到的返回值进行格式化并取值判断
        res = json.loads(info)
        print(res)
        if self.case_name == "getPrevsearchordercredits":
            self.assertEqual(res['Code'], "000000")


if __name__ == "__main__":
    testT.test()

