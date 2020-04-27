# coding:utf-8
"""收费报表"""
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
        print("---------------收费报表测试开始----------------------")
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

    def test_36(self):
        '''进入收费报表'''
        print("\n--------------用例36------------------")
        try:
            print("进入后台管理")
            time.sleep(20)
            print("进入收费报表")
            self.lo.Charge_statemen()
            time.sleep(2)
            # 断言
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(16,1)),self.dr.Assert2(xlrd.read_excel_three(16,2)))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_37(self):
        '''临停收费记录导出'''
        print("\n--------------用例37------------------")
        try:
            time.sleep(2)
            print("点击进入临停收费记录")
            self.dr.Clickxpath(xlrd.read_excel_two(122,1))
            time.sleep(2)
            print("选择开始时间")
            self.dr.send_keysid(xlrd.read_excel_two(137,1),xlrd.read_excel_two(137,1),xlrd.read_excel(78,5))
            print("选择结束时间")
            self.dr.send_keysid(xlrd.read_excel_two(138,1),xlrd.read_excel_two(138,1),xlrd.read_excel(79,5))
            print("点击查询")
            self.dr.Clickxpath(xlrd.read_excel_two(145,1))
            time.sleep(5)
            print("点击导出")
            self.dr.Clickxpath(xlrd.read_excel_two(123,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(17,1))
            print("用例结束")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_38(self):
        '''退款记录导出'''
        print("\n--------------用例38------------------")
        try:
            time.sleep(2)
            print("点击进入退款记录")
            self.dr.Clickxpath(xlrd.read_excel_two(124,1))
            time.sleep(2)
            print("选择开始时间")
            self.dr.send_keysid(xlrd.read_excel_two(139,1),xlrd.read_excel_two(139,1),xlrd.read_excel(80,5))
            print("选择结束时间")
            self.dr.send_keysid(xlrd.read_excel_two(140,1),xlrd.read_excel_two(140,1),xlrd.read_excel(81,5))
            print("点击查询")
            self.dr.Clickxpath(xlrd.read_excel_two(146,1))
            time.sleep(5)
            print("点击导出")
            self.dr.Clickxpath(xlrd.read_excel_two(125,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(18,1))
            print("用例结束")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_39(self):
        '''特殊车辆收费记录导出'''
        print("\n--------------用例39------------------")
        try:
            time.sleep(2)
            print("无人用特殊车辆收费记录，没有写，过")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_40(self):
        '''包期充值记录记录导出'''
        print("\n--------------用例40------------------")
        try:
            time.sleep(2)
            print("点击进入包期车充值记录")
            self.dr.Clickxpath(xlrd.read_excel_two(128,1))
            time.sleep(2)
            print("选择开始时间")
            self.dr.send_keysid(xlrd.read_excel_two(141,1),xlrd.read_excel_two(141,1),xlrd.read_excel(84,5))
            print("选择结束时间")
            self.dr.send_keysid(xlrd.read_excel_two(142,1),xlrd.read_excel_two(142,1),xlrd.read_excel(85,5))
            print("点击查询")
            self.dr.Clickxpath(xlrd.read_excel_two(147,1))
            time.sleep(5)
            print("点击导出")
            self.dr.Clickxpath(xlrd.read_excel_two(129,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(19,1))
            print("用例结束")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_41(self):
        '''收费合计导出'''
        print("\n--------------用例41------------------")
        try:
            time.sleep(2)
            print("点击进入退款记录")
            self.dr.Clickxpath(xlrd.read_excel_two(130,1))
            time.sleep(2)
            print("选择开始时间")
            self.dr.send_keysid(xlrd.read_excel_two(143,1),xlrd.read_excel_two(143,1),xlrd.read_excel(86,5))
            print("选择结束时间")
            self.dr.send_keysid(xlrd.read_excel_two(144,1),xlrd.read_excel_two(144,1),xlrd.read_excel(87,5))
            print("点击查询")
            self.dr.Clickxpath(xlrd.read_excel_two(148,1))
            time.sleep(5)
            print("点击导出")
            self.dr.Clickxpath(xlrd.read_excel_two(131,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(20,1))
            print("用例结束")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


if __name__ == '__main__':
    unittest.main()
