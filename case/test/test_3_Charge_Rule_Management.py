# coding:utf-8
"""收费规则管理"""
import sys,os
sys.path.append('E:\\huangye')
import unittest
import time
from selenium import webdriver
from case.test_case.Auxiliary.auxiliary import Driver
from case.test_case.Login.login import Login
from case.common.excel.xlrd import xlrd
from case.common.Mysql.mysql import MySQL


class Test_Chaege_Rule(unittest.TestCase):

    # 类开始前执行一次
    @classmethod
    def setUpClass(cls) :
        driver = webdriver.Chrome('C:\\Users\\ChenYang\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.maximize_window()
        print("---------------收费规则管理测试开始----------------------")
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
        print("测试结束，已退出浏览器")

    # 每个用例开始前执行一次
    def setUp(self):
        pass
    # 每个用例结束后执行一次
    def tearDown(self):
        pass


    def test_10(self):
        '''进入收费规则管理'''
        print("\n--------------用例10------------------")
        try:
            print("进入后台管理系统")
            time.sleep(20)
            # 进入收费规则管理管理
            print("进入收费规则管理")
            self.lo.Charge_Management()
            time.sleep(3)
            # 断言
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(9,1)),self.dr.Assert2(xlrd.read_excel_three(9,2)))
            print("用例成功")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_11(self):
        '''添加普通临停车收费规则'''
        print("--------------用例11------------------")
        try:
            time.sleep(2)
            print("点击普通临停车收费规则")
            self.dr.Clickxpath(xlrd.read_excel_two(27,1))
            time.sleep(8)
            print("输入规则名称")
            self.dr.send_keysname(xlrd.read_excel_two(29,1),xlrd.read_excel(25,5))
            print("输入免费停车时长")
            self.dr.send_keysname(xlrd.read_excel_two(30,1),xlrd.read_excel(26,5))
            print("输入首段收费时长")
            self.dr.send_keysname(xlrd.read_excel_two(31,1),xlrd.read_excel(27,5))
            print("输入间隔收费时长")
            self.dr.send_keysname(xlrd.read_excel_two(32,1),xlrd.read_excel(28,5))
            print("输入首段收费金额")
            self.dr.send_keysname(xlrd.read_excel_two(33,1),xlrd.read_excel(29,5))
            print("输入间隔收费金额")
            self.dr.send_keysname(xlrd.read_excel_two(34,1),xlrd.read_excel(30,5))
            print("下拉框选择车辆类型为小型车")
            self.dr.drop_down(xlrd.read_excel_two(35,1),xlrd.read_excel_two(36,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(37,1))
            time.sleep(10)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(38,1))
            time.sleep(5)
            print("通过数据库确认是否添加成功进行断言")
            MySQL.Mysql(xlrd.read_excel_four(1,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_12(self):
        '''删除普通临停车收费规则'''
        print("--------------用例12------------------")
        try:
            time.sleep(2)
            print("点击普通临停车收费规则删除按钮")
            self.dr.Clickxpath(xlrd.read_excel_two(39,1))
            time.sleep(1)
            print("点击确定")
            self.dr.Clickid(xlrd.read_excel_two(23,1))
            time.sleep(1)
            print("再次点击确定")
            self.dr.Clickxpath(xlrd.read_excel_two(24,1))
            print("删除成功")
            time.sleep(1)
            print("通过数据库确认是否删除成功进行断言")
            MySQL.Mysql_delete(xlrd.read_excel_four(1,1))
            print("用例成功")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_13(self):
        '''添加固定临停车收费规则'''
        print("--------------用例13------------------")
        try:
            time.sleep(2)
            print("点击固定临停车收费规则")
            self.dr.Clickxpath(xlrd.read_excel_two(28,1))
            time.sleep(2)
            print("输入规则名称")
            self.dr.send_keysname(xlrd.read_excel_two(29,1),xlrd.read_excel(34,5))
            print("输入免费停车时长")
            self.dr.send_keysname(xlrd.read_excel_two(30,1),xlrd.read_excel(35,5))
            print("输入首段收费时长")
            self.dr.send_keysname(xlrd.read_excel_two(31,1),xlrd.read_excel(36,5))
            print("输入间隔收费时长")
            self.dr.send_keysname(xlrd.read_excel_two(32,1),xlrd.read_excel(37,5))
            print("输入首段收费金额")
            self.dr.send_keysname(xlrd.read_excel_two(33,1),xlrd.read_excel(38,5))
            print("输入间隔收费金额")
            self.dr.send_keysname(xlrd.read_excel_two(34,1),xlrd.read_excel(39,5))
            print("下拉框选择车辆类型为小型车")
            self.dr.drop_down(xlrd.read_excel_two(35,1),xlrd.read_excel_two(36,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(37,1))
            time.sleep(5)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(38,1))
            time.sleep(10)
            print("通过数据库确认是否添加成功进行断言")
            MySQL.Mysql(xlrd.read_excel_four(2,1))
            print("用例成功")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_14(self):
        '''删除固定临停车收费规则'''
        print("--------------用例14------------------")
        try:
            time.sleep(2)
            print("点击固定临停车收费规则删除按钮")
            self.dr.Clickxpath(xlrd.read_excel_two(39,1))
            time.sleep(1)
            print("点击确定")
            self.dr.Clickid(xlrd.read_excel_two(23,1))
            time.sleep(1)
            print("再次点击确定")
            self.dr.Clickxpath(xlrd.read_excel_two(24,1))
            print("删除成功")
            time.sleep(1)
            print("通过数据库确认是否删除成功进行断言")
            MySQL.Mysql_delete(xlrd.read_excel_four(2,1))

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise



# if __name__ == '__main__':
#     unittest.main()
