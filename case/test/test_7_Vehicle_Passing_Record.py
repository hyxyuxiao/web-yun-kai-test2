# coding:utf-8
"""过车记录查询"""
import sys,os
sys.path.append('E:\\huangye')
import unittest
import time
from selenium import webdriver
from case.test_case.Auxiliary.auxiliary import Driver
from case.test_case.Login.login import Login
from case.common.excel.xlrd import xlrd
from case.common.Mysql.mysql import MySQL

class Charge_Statement(unittest.TestCase):

    # 类开始前执行一次
    @classmethod
    def setUpClass(cls) :
        driver = webdriver.Chrome('C:\\Users\\ChenYang\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.maximize_window()
        print("---------------过车记录查询测试开始----------------------")
        # 获取辅助功能driver
        cls.dr = Driver(driver)
        # 获取login的driver
        cls.lo = Login(driver)
        # 打开网页，读取excel文档内容3列3行url
        cls.dr.open_url(xlrd.read_excel(1,3))
        time.sleep(2)
        # 登录后台
        cls.lo.login()


    # 类结束后执行一次
    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls.dr.quit_web()
        print("\n测试结束，已退出浏览器")

    # 每个用例开始前执行一次
    def setUp(self):
        pass
    # 每个用例结束后执行一次
    def tearDown(self):
        pass

    def test_42(self):
        '''进入过车记录查询'''
        print("\n--------------用例42------------------")
        try:
            print("进入后台管理")
            time.sleep(20)
            print("进入过车记录查询")
            self.lo.Vehicle_Passing_record()
            time.sleep(2)
            # 断言
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(22,1)),self.dr.Assert2(xlrd.read_excel_three(22,2)))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise



    def test_43(self):
        '''导出过车记录信息'''
        print("\n--------------用例43------------------")
        try:
            time.sleep(2)
            print("点击进入过车记录")
            self.dr.Clickxpath(xlrd.read_excel_two(133,1))
            time.sleep(2)
            print("选择开始时间")
            self.dr.send_keysid(xlrd.read_excel_two(135,1),xlrd.read_excel_two(135,1),xlrd.read_excel(90,5))
            print("选择结束时间")
            self.dr.send_keysid(xlrd.read_excel_two(136,1),xlrd.read_excel_two(136,1),xlrd.read_excel(91,5))
            print("点击查询")
            self.dr.Clickxpath(xlrd.read_excel_two(149,1))
            time.sleep(5)
            print("点击导出")
            self.dr.Clickxpath(xlrd.read_excel_two(134,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(23,1))
            print("用例结束")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_44(self):
        '''过车记录下载模板'''
        print("\n--------------用例44------------------")
        try:
            time.sleep(2)
            print("点击下载模板")
            self.dr.Clickxpath(xlrd.read_excel_two(150,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu_xlsx(xlrd.read_excel_three(24,1))

            print("用例结束")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_45(self):
        '''过车记录信息导入'''
        print("\n--------------用例45------------------")
        try:
            time.sleep(2)
            print("点击导入")
            self.dr.Clickxpath(xlrd.read_excel_two(151,1))
            print("打开选择文件，导入文件")
            self.dr.send_keysdao(xlrd.read_excel_two(152,1),xlrd.read_excel(93,5))
            time.sleep(2)
            print("点击保存")
            self.dr.Clickid(xlrd.read_excel_two(153,1))
            time.sleep(5)
            print("保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(154,1))
            time.sleep(2)
            print("关闭导入框")
            self.dr.Clickxpath(xlrd.read_excel_two(161,1))
            time.sleep(4)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(20,1))
            print("用例完成")


        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise
