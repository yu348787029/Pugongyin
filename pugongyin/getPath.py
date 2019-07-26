import os

def get_basepath():
    #获取当前项目文件绝对路径
    #这样的做目的：直接获取项目路径，方便使用，后面文件直接拿过去引用
    basepath = os.path.split(os.path.realpath(__file__))[0]
    return basepath

'''
    if __name__ == '__main__':
    print('当前项目文件绝对路径为：',os.path.split(os.path.realpath(__file__))[0])

'''