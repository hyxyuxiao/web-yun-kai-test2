import os

def deleteHTML():
    '''删除html日志'''
    # 需要把路径替换成你的文件夹所在路径
    path = 'E:/huangye/case/report/report'
    # 利用os模块中的listdir函数和for语句，浏览所有文件
    files = os.listdir(path)
    for f in files:
        # 判断文件是否符合要求
        if(f.endswith('.html') and ("UI自动化") in f):
            # 如果符合要求，则输出文件名
            print("html文件名：%s" %f)
            print("删除文件")
            os.remove('E:/huangye/case/report/report/%s'% f)
            print("删除成功")

def deletePNG():
    '''删除png日志'''
    # 需要把路径替换成你的文件夹所在路径
    path = 'E:/huangye/case/report/report/images'
    # 利用os模块中的listdir函数和for语句，浏览所有文件
    files = os.listdir(path)
    for f in files:
        # 判断文件是否符合要求
        if(f.endswith('.png') and ("2019")in f):
            # 如果符合要求，则输出文件名
            print("png文件名：%s" %f)
            print("删除文件")
            os.remove('E:/huangye/case/report/report/images/%s'% f)
            print("删除成功")

def deleteZIP():
    '''删除zip日志'''
    # 需要把路径替换成你的文件夹所在路径
    path = 'E:/huangye/case/report/'
    # 利用os模块中的listdir函数和for语句，浏览所有文件
    files = os.listdir(path)
    for f in files:
        # 判断文件是否符合要求
        if(f.endswith('.zip') and ("UI自动化") in f):
            # 如果符合要求，则输出文件名
            print("zip文件名：%s" %f)
            print("删除文件")
            os.remove('E:/huangye/case/report/%s'% f)
            print("删除成功")
