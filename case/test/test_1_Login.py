# coding:utf-8
"""登录测试"""
import os,sys,logging
sys.path.append('E:\\huangye')
import unittest
import time
from selenium import webdriver
from case.test_case.Auxiliary.auxiliary import Driver
from case.test_case.Login.login import Login
from case.common.excel.xlrd import xlrd


#创建logger，如果参数为空则返回root logger
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)  #设置logger日志等级



class Test_Login(unittest.TestCase):

    # 类开始前执行一次
    @classmethod
    def setUpClass(cls) :
        print("---------------登录测试开始----------------------")

    def setUp(self):
        driver = webdriver.Chrome('C:\\Users\\ChenYang\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.maximize_window()
        self.dr = Driver(driver)
        self.lo = Login(driver)
        # 打开网页，读取excel文档内容1行3列url
        self.dr.open_url(xlrd.read_excel(1,3))

    def tearDown(self):
        self.dr.quit_web()


    # 类结束后执行一次
    @classmethod
    def tearDownClass(cls):
        pass

    def test_01(self):
        '''输入正确的账号密码'''
        print("--------------用例1------------------")
        try:
            time.sleep(2)
            # 登录后台
            logger.info("登录后台")
            self.lo.login()
            time.sleep(4)
            logger.info("开始断言")
            # 断言，读取excel文档内容
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(1,1)),self.dr.Assert2(xlrd.read_excel_three(1,2)))
            logger.info("用例成功")
        except Exception as msg:

            logger.info("异常原因%s"%msg)
            self.dr.getImage()
            # raise抛出异常
            raise


    def test_02(self):
        '''输入错误的账号密码'''
        print("--------------用例2------------------")
        try:
            time.sleep(2)
            # 登录后台
            # 输入账号，读取excel文档内容
            logger.info("输入正确的账号")
            self.dr.send_keysid(xlrd.read_excel_two(1,1),xlrd.read_excel_two(1,1),xlrd.read_excel(4,5))
            logger.info("输入错误的密码")
            # 输入密码，读取excel文档内容
            logger.info("错误的密码：%s" %xlrd.read_excel(5,5))
            self.dr.send_keysid(xlrd.read_excel_two(2,1),xlrd.read_excel_two(2,1),xlrd.read_excel(5,5))
            # 点击确定，读取excel文档内容
            logger.info("点击确认")
            self.dr.Clickid(xlrd.read_excel_two(3,1))
            time.sleep(2)
            # 断言文本是否正确，读取excel文档内容
            logger.info("开始断言")
            self.dr.is_login_sucess(xlrd.read_excel_three(2,1))
            logger.info("用例成功")
        except Exception as msg:

            logger.info("异常原因%s"%msg)
            self.dr.getImage()
            # raise抛出异常
            raise



if __name__ == '__main__':
     unittest.main()
