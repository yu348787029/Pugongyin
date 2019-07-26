import os
import common.HTMLTestRunner as HTMLTestRunner
import read.readConfig as readConfig
import getPath
import unittest

basepath = getPath.get_basepath()
report_path = os.path.join(basepath,'result')

class AllTest:
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path,'report.html')
        self.caseListFile = os.path.join(basepath,'test_file\caselist.txt')
        self.caseFile = os.path.join(basepath,'test_case')
        self.caseList = []

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            # 如果data非空且不以#开头
            if data != '' and not data.startswith('#'):
                # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
                self.caseList.append(data.replace("\n",""))
        fb.close()

    def set_case_suite(self):
        # 通过set_case_list()拿到caselist元素组
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        # 从caselist元素组中循环取出case
        for case in self.caseList:
            # 通过split函数来将user/login_case分割字符串，-1取后面，0取前面
            case_name = case.split("/")[-1]
            # 打印出取出来的名称
            print(case_name+'.py')
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名 参考这个  https://blog.csdn.net/happyuu/article/details/80683161
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name+'.py',top_level_dir=None)
            # 将discover存入suite_module元素
            suite_module.append(discover)
            # 判断suite_module元素组是否存在元素
        if len(suite_module)>0:
            # 如果存在，循环取出元素组内容，命名为suite
            for suite in suite_module:
                # 从discover中取出test_name，使用addTest添加到测试集
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            # 调用set_case_suite获取test_suite
            suit = self.set_case_suite()
            print ("suit:",suit)
            # 判断test_suite是否为空
            if suit is not None:
                # 打开result/report.html测试报告文件，如果不存在就创建
                fp = open(resultPath,'wb')
                # 调用HTMLTestRunner  这个文件不用管  网上有可以直接下载的
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="测试说明")
                runner.run(suit)
            else:
                print("没有案例可以测试")
        finally:
            on_off = readConfig.ReadConfig().get_email('on_off')
            if on_off =='on':
                #configEmail.Email().send_email()
                print("发送邮件")

            elif on_off == 'off':
                print('发送邮件已关闭')
            fp.close()

if __name__=="__main__":
    AllTest().run()