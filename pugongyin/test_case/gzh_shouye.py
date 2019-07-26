import json
import unittest
import paramunittest
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
from test_case.gzh_login import testT

class testgzhshouye():


    def aaa(self):
        testT.test()
        print("哎哎哎哎", testT.get_value('ShipOwnerId'))

if __name__ == '__main__':
    print("`111")
    print("哎哎哎哎", testT.get_value('ShipOwnerId'))
    testgzhshouye.aaa
