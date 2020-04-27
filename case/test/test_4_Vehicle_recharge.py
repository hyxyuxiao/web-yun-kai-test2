# coding:utf-8
"""车辆管理"""
import sys,os
sys.path.append('E:\\huangye')
import unittest
import time
from selenium import webdriver
from case.test_case.Auxiliary.auxiliary import Driver
from case.test_case.Login.login import Login
from case.common.excel.xlrd import xlrd
from case.common.Mysql.mysql import MySQL


class Vehicle_and_recharge(unittest.TestCase):

    # 类开始前执行一次
    @classmethod
    def setUpClass(cls) :
        driver = webdriver.Chrome('C:\\Users\\ChenYang\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.maximize_window()
        print("---------------车辆与充值管理测试开始----------------------")
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


    def test_15(self):
        '''进入车辆与充值管理'''
        print("\n--------------用例15------------------")
        try:
            print("进入后台管理")
            time.sleep(20)
            print("进入车辆与充值管理界面")
            self.lo.Vehicles_and_recharge()
            time.sleep(2)
            # 断言
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(10,1)),self.dr.Assert2(xlrd.read_excel_three(10,2)))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_16(self):
        '''添加包期车'''
        print("--------------用例16------------------")
        try:
            time.sleep(2)
            print("点击添加")
            self.dr.Clickxpath(xlrd.read_excel_two(42,1))
            time.sleep(8)
            print("输入车牌号")
            self.dr.send_keysname(xlrd.read_excel_two(43,1),xlrd.read_excel(45,5))
            time.sleep(2)
            print("输入车主姓名")
            self.dr.send_keysname(xlrd.read_excel_two(44,1),xlrd.read_excel(46,5))
            time.sleep(1)
            print("输入联系电话")
            self.dr.send_keysname(xlrd.read_excel_two(45,1),xlrd.read_excel(47,5))
            print("点击车位编号")
            self.dr.Clickxpath(xlrd.read_excel_two(46,1))
            time.sleep(1)
            print("输入车位编号")
            self.dr.send_keysid(xlrd.read_excel_two(47,1),xlrd.read_excel_two(47,1),xlrd.read_excel(48,5))
            print("点击查询")
            self.dr.Clickxpath(xlrd.read_excel_two(48,1))
            time.sleep(1)
            print("点击选择该车位")
            self.dr.Clickxpath(xlrd.read_excel_two(49,1))
            time.sleep(3)
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(50,1))
            time.sleep(3)
            print("点击保存确认")
            self.dr.Clickxpath(xlrd.read_excel_two(51,1))
            time.sleep(2)
            print("开始断言")
            # 数据库中查询该车辆是否已经添加
            MySQL.Mysql(xlrd.read_excel_four(3,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_17(self):
        '''包期车充值'''
        print("--------------用例17------------------")
        try:
            time.sleep(2)
            print("搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(62,1),xlrd.read_excel_two(62,1),xlrd.read_excel(45,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(53,1))
            time.sleep(2)
            print("点击充值")
            self.dr.Clickxpath(xlrd.read_excel_two(57,1))
            time.sleep(2)
            print("选择充值规则")
            self.dr.drop_down(xlrd.read_excel_two(58,1),xlrd.read_excel_two(59,1))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(60,1))
            time.sleep(2)
            print("开始断言")
            # 数据库中查询该车辆是否已经充值
            # MySQL.Mysql(xlrd.read_excel_four(5,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_18(self):
        '''包期车修改为VIP车'''
        print("--------------用例18------------------")
        try:
            time.sleep(2)
            print("搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(62,1),xlrd.read_excel_two(62,1),xlrd.read_excel(45,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(53,1))
            time.sleep(2)
            print("车辆编辑")
            self.dr.Clickxpath(xlrd.read_excel_two(54,1))
            time.sleep(1)
            print("修改为VIP车")
            self.dr.drop_down(xlrd.read_excel_two(55,1),xlrd.read_excel_two(56,1))
            time.sleep(2)
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(50,1))
            time.sleep(2)
            print("点击保存确认")
            self.dr.Clickxpath(xlrd.read_excel_two(51,1))
            time.sleep(2)
            print("开始断言")
            # 数据库中查询该车辆是否修改成VIP车
            MySQL.Mysql(xlrd.read_excel_four(5,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_19(self):
        '''VIP车修改为固定临停车'''
        print("--------------用例19------------------")
        try:
            time.sleep(2)
            print("搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(62,1),xlrd.read_excel_two(62,1),xlrd.read_excel(45,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(53,1))
            time.sleep(2)
            print("车辆编辑")
            self.dr.Clickxpath(xlrd.read_excel_two(54,1))
            time.sleep(2)
            print("修改为固定临停车")
            self.dr.drop_down(xlrd.read_excel_two(55,1),xlrd.read_excel_two(61,1))
            time.sleep(2)
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(50,1))
            time.sleep(2)
            print("点击保存确认")
            self.dr.Clickxpath(xlrd.read_excel_two(51,1))
            time.sleep(2)
            print("开始断言")
            # 数据库中查询该车辆是否修改成固定临停车
            MySQL.Mysql(xlrd.read_excel_four(6,1))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_20(self):
        '''固定临停车充值'''
        print("--------------用例20------------------")
        try:
            time.sleep(2)
            print("搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(62,1),xlrd.read_excel_two(62,1),xlrd.read_excel(45,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(53,1))
            time.sleep(2)
            print("点击充值")
            self.dr.Clickxpath(xlrd.read_excel_two(63,1))
            time.sleep(2)
            print("输入充值金额")
            self.dr.send_keysname(xlrd.read_excel_two(64,1),xlrd.read_excel(58,5))
            print("点击保存")
            self.dr.Clickxpath(xlrd.read_excel_two(65,1))
            time.sleep(2)
            print("点击保存确定")
            self.dr.Clickxpath(xlrd.read_excel_two(66,1))
            time.sleep(1)
            print("开始断言")
            # self.dr.text_duanyan(xlrd.read_excel_three(11,1),xlrd.read_excel_three(11,2))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_21(self):
        '''删除车辆信息'''
        print("--------------用例21------------------")
        try:
            time.sleep(1)
            print("搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(62,1),xlrd.read_excel_two(62,1),xlrd.read_excel(45,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(53,1))
            time.sleep(2)
            print("勾选车辆")
            self.dr.Clickxpath(xlrd.read_excel_two(67,1))
            print("点击删除")
            self.dr.Clickxpath(xlrd.read_excel_two(68,1))
            time.sleep(2)
            print("删除确定")
            self.dr.Clickxpath(xlrd.read_excel_two(69,1))
            time.sleep(2)
            print("开始断言")
            # 数据库中查询该车辆是否被删除
            MySQL.Mysql_delete(xlrd.read_excel_four(7,1))
            print("用例成功")


        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise



    def test_22(self):
        '''固定临停车撤单'''
        print("--------------用例22------------------")
        try:
            time.sleep(2)
            print("进入固定临停车充值统计")
            self.lo.Recharge_statistics()
            print("搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(72,1),xlrd.read_excel_two(72,1),xlrd.read_excel(60,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(73,1))
            time.sleep(2)
            print("点击撤单")
            self.dr.Clickxpath(xlrd.read_excel_two(74,1))
            time.sleep(1)
            print("输入备注")
            self.dr.send_keysname(xlrd.read_excel_two(75,1),xlrd.read_excel(61,5))
            time.sleep(1)
            print("撤单确定")
            self.dr.Clickxpath(xlrd.read_excel_two(76,1))
            time.sleep(1)
            print("撤单成功确定")
            self.dr.Clickxpath(xlrd.read_excel_two(77,1))
            print("撤单完成")
            time.sleep(2)

            print("开始断言")
            print("再次搜索车牌")
            self.dr.send_keysid(xlrd.read_excel_two(72,1),xlrd.read_excel_two(72,1),xlrd.read_excel(60,5))
            print("查询")
            self.dr.Clickxpath(xlrd.read_excel_two(73,1))
            time.sleep(2)
            self.dr.text_duanyan(xlrd.read_excel_three(12,1),xlrd.read_excel_three(12,2))
            print("断言成功，用例完成")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            raise



if __name__ == '__main__':
    unittest.main()
