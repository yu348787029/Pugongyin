import os
import configparser
import getPath as getpath

#引用路径获取文件然后调用
#然后使用 os.path.join把路径拼接全
basepath = getpath.get_basepath()
config_path = os.path.join(basepath,'config\config.ini')
config = configparser.ConfigParser()#实例化
config.read(config_path)

class ReadConfig():
    #获取config文件中名字为 [HTTP] 的属性值
    def get_http(self,name):
        value = config.get('HTTP' , name)
        return value
    # 获取config文件中名字为 [EMAIL] 的属性值
    def get_email(self,name):
        value = config.get('EMAIL' , name)
        return value
    # 获取config文件中名字为 [DATABASE] 的属性值
    def get_database(self,name):
        value = config.get('DATABASE' , name)
        return value

