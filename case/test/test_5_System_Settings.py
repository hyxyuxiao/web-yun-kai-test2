# coding:utf-8
"""系统设置"""
import sys,os
sys.path.append('E:\\huangye')
import unittest
import time
from selenium import webdriver
from case.test_case.Auxiliary.auxiliary import Driver
from case.test_case.Login.login import Login
from case.common.excel.xlrd import xlrd
from case.common.Mysql.mysql import MySQL


class System_Settings(unittest.TestCase):

    # 类开始前执行一次
    @classmethod
    def setUpClass(cls) :
        driver = webdriver.Chrome('C:\\Users\\ChenYang\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.maximize_window()
        print("---------------系统设置测试开始----------------------")
        # 获取辅助功能driver
        cls.dr = Driver(driver)
        # 获取login的driver
        cls.lo = Login(driver)
        # 打开网页，读取excel文档内容3列3行url
        cls.dr.open_url(xlrd.read_excel(1,3))
        time.sleep(2)
        # 登录后台
        cls.lo.login()
        # 开始运行前删除数据库中的所有表
        MySQL.Mysql_delete_tables(xlrd.read_excel_four(51,1))
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


    def test_23(self):
        '''进入系统设置'''
        print("\n--------------用例23------------------")
        try:
            print("进入后台管理")
            time.sleep(20)
            print("进入系统设置")
            self.lo.System_settings()
            time.sleep(2)
            # 断言
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(14,1)),self.dr.Assert2(xlrd.read_excel_three(14,2)))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_24(self):
        '''找零配置-少收记账，下次停车进行追缴'''
        print("\n--------------用例24------------------")
        try:
            time.sleep(2)
            print("勾选少收记账，下次停车进行追缴")
            self.dr.Clickxpath(xlrd.read_excel_two(82,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(86,1))
            time.sleep(3)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(87,1))
            time.sleep(5)
            print("开始断言")
            MySQL.Mysql_two(xlrd.read_excel_four(8,1),xlrd.read_excel_four(8,2),xlrd.read_excel_four(8,3))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_25(self):
        '''找零配置-少收记账，但不进行追缴'''
        print("\n--------------用例25------------------")
        try:
            time.sleep(2)
            print("勾选少收记账，但不进行追缴")
            self.dr.Clickxpath(xlrd.read_excel_two(83,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(86,1))
            time.sleep(3)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(87,1))
            time.sleep(4)
            print("开始断言")
            MySQL.Mysql_two(xlrd.read_excel_four(9,1),xlrd.read_excel_four(9,2),xlrd.read_excel_four(9,3))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise



    def test_26(self):
        '''找零配置-多收记账，并充值到余额'''
        print("\n--------------用例26------------------")
        try:
            time.sleep(2)
            print("勾选多收记账，并充值到余额")
            self.dr.Clickxpath(xlrd.read_excel_two(84,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(86,1))
            time.sleep(3)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(87,1))
            time.sleep(2)
            print("开始断言")
            MySQL.Mysql_two(xlrd.read_excel_four(10,1),xlrd.read_excel_four(10,2),xlrd.read_excel_four(10,3))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_27(self):
        '''找零配置-多收记账，下次停车抵扣'''
        print("\n--------------用例27------------------")
        try:
            time.sleep(2)
            print("勾选多收记账，下次停车抵扣")
            self.dr.Clickxpath(xlrd.read_excel_two(85,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(86,1))
            time.sleep(3)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(87,1))
            time.sleep(2)
            print("开始断言")
            MySQL.Mysql_two(xlrd.read_excel_four(11,1),xlrd.read_excel_four(11,2),xlrd.read_excel_four(11,3))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_28(self):
        '''访客-黑白名单配置'''
        print("\n--------------用例28------------------")
        try:
            time.sleep(2)
            print("点击访客-黑白名单配置")
            self.dr.Clickxpath(xlrd.read_excel_two(88,1))
            print("勾选启用访客放行")
            print("勾选启用黑名单")
            print("勾选启用白名单")
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(89,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(90,1))
            time.sleep(2)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(12,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_29(self):
        '''优惠券配置'''
        print("\n--------------用例29------------------")
        try:
            time.sleep(2)
            print("点击优惠券配置")
            self.dr.Clickxpath(xlrd.read_excel_two(91,1))
            print("勾选转成“现金券”")
            self.dr.Clickxpath_select(xlrd.read_excel_two(92,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(93,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(94,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(13,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_30(self):
        '''已过期计费配置'''
        print("\n--------------用例30------------------")
        try:

            time.sleep(2)
            print("点击已过期计费配置")
            self.dr.Clickxpath(xlrd.read_excel_two(95,1))
            print("勾选已过期缴费出场配置")
            self.dr.Clickxpath_select(xlrd.read_excel_two(96,1))
            print("点击保存")
            self.dr.Clickxpath_last(xlrd.read_excel_two(97,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(98,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(14,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_30_1(self):
        '''推送过车消息到公众号'''
        print("\n--------------用例30_1------------------")
        try:
            time.sleep(2)
            print("点击推送过车消息到公众号")
            self.dr.Clickxpath(xlrd.read_excel_two(156,1))
            print("勾选启用消息推送")
            self.dr.Clickxpath_select(xlrd.read_excel_two(157,1))
            print("输入过车地点")
            self.dr.send_keys(xlrd.read_excel_two(158,1),xlrd.read_excel_two(158,1),xlrd.read_excel(95,5))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(159,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(160,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(21,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_31(self):
        '''无牌车核销配置'''
        print("\n--------------用例31------------------")
        try:
            time.sleep(2)
            print("点击进入停车场")
            self.dr.Clickid(xlrd.read_excel_two(7,1))
            time.sleep(1)
            print("点击无牌车核销配置")
            self.dr.Clickxpath(xlrd.read_excel_two(99,1))
            print("输入核销天数")
            self.dr.send_keysname(xlrd.read_excel_two(100,1),xlrd.read_excel(71,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(101,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(102,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(15,1))
            print("用例成功")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise



    def test_32(self):
        '''所有车牌记车位'''
        print("\n--------------用例32------------------")
        try:
            time.sleep(2)
            print("点击所有车牌记车位")
            self.dr.Clickxpath(xlrd.read_excel_two(103,1))
            print("勾选所有车牌记车位")
            self.dr.Clickxpath_select(xlrd.read_excel_two(104,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(105,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(106,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(16,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_33(self):
        '''抓拍配置'''
        print("\n--------------用例33------------------")
        try:
            time.sleep(2)
            print("点击抓拍配置")
            self.dr.Clickxpath(xlrd.read_excel_two(107,1))
            print("勾选地感抓拍")
            self.dr.Clickxpath_select(xlrd.read_excel_two(108,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(109,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(110,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(17,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_34(self):
        '''冲卡配置'''
        print("\n--------------用例34------------------")
        try:
            time.sleep(2)
            print("点击冲卡配置")
            self.dr.Clickxpath(xlrd.read_excel_two(111,1))
            print("勾选处理冲卡车辆")
            self.dr.Clickxpath_select(xlrd.read_excel_two(112,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(113,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(114,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(18,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_35(self):
        '''非系统放行记车位-记车位'''
        print("\n--------------用例35------------------")
        try:
            time.sleep(2)
            print("点击非系统放行记车位")
            self.dr.Clickxpath(xlrd.read_excel_two(115,1))
            print("勾选记车位")
            self.dr.Clickxpath_select(xlrd.read_excel_two(116,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(117,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(118,1))
            time.sleep(1)
            print("开始断言")
            MySQL.Mysql(xlrd.read_excel_four(19,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

# if __name__ == '__main__':
#     unittest.main()
