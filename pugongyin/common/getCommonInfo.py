import requests
import read.readConfig as readConfig
import json
from common.configHttp import RunMain
import unittest



url = readConfig.ReadConfig().get_http("gzhonlineurl")#获取配置文件中的url地址

response = requests.get(url+'/api/login/detail?token=gzhlogin:0f289302-3cbd-4a5a-8e47-edd071a0a1d0')


versionInfo = response.text

versionInfoPython = json.loads(versionInfo)

dataList = versionInfoPython.get('Data')

shipOwnerId = dataList.get('ShipOwnerId')

goods = requests.get(url+'/api/ware/'+shipOwnerId+'/shipowner/alllist')

goodsInfo = goods.text

goodsList = json.loads(goodsInfo).get('Data')

WareDTOs = goodsList.get('WareDTOs')

wareId = WareDTOs[0].get('Id')

def getShipOwnerId():
    return shipOwnerId

def getWareId():
    return wareId


