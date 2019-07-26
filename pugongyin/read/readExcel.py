import os
import getPath
from xlrd import open_workbook

basepath = getPath.get_basepath()
class ReadExcel():
    def get_xls(self,xls_name,sheet_name):
        cls = []
        #拼接文件路径
        xlsPath = os.path.join(basepath,'test_file','case',xls_name)
        #打开文件  login.xls
        file = open_workbook(xlsPath)
        #获取sheet  也就是 login.xls文件的 sheet名字
        sheet = file.sheet_by_name(sheet_name)
        #获取行数
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                #获取整行 整列的值  返回必须是数字 所以上面有空的 cls数组
                #获取excel表格中的isTest中的值是否是Y，是的话则获取该行，
                if sheet.row_values(i)[4]=="Y":
                    cls.append(sheet.row_values(i))
        return cls