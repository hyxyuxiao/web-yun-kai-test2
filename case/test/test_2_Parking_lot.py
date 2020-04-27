# coding:utf-8
"""车位管理测试"""
import sys,os
sys.path.append('E:\\huangye')
import unittest
import time
from selenium import webdriver
from case.test_case.Auxiliary.auxiliary import Driver
from case.test_case.Login.login import Login
from case.common.excel.xlrd import xlrd
import logging


#创建logger，如果参数为空则返回root logger
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)  #设置logger日志等级






class Test_Parking_lot_Login(unittest.TestCase):

    # 类开始前执行一次
    @classmethod
    def setUpClass(cls) :
        driver = webdriver.Chrome('C:\\Users\\ChenYang\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        driver.maximize_window()
        print("---------------车位管理测试开始----------------------")
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


    def test_03(self):
        '''进入车位管理'''
        print("--------------用例3------------------")
        try:
            print("进入后台管理系统")
            time.sleep(20)
            # 进入车位管理
            print("进入车位管理")
            self.lo.Parking_Management()
            time.sleep(3)
            # 断言
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(3,1)),self.dr.Assert2(xlrd.read_excel_three(3,2)))
            print("用例成功")
        except Exception as msg:
            self.dr.getImage()
            logger.info("异常原因%s"%msg)
            # raise抛出异常
            raise


    def test_04(self):
        '''添加新的车位'''
        print("--------------用例4------------------")
        try:
            time.sleep(2)
            print("点击添加")
            self.dr.Clickid(xlrd.read_excel_two(8,1))
            time.sleep(5)
            print("添加新车位")
            # 输入业主名称
            print("输入业主名称")
            self.dr.send_keysname(xlrd.read_excel_two(9,1),xlrd.read_excel(12,5))
            # 输入车位号
            print("输入车位号")
            self.dr.send_keysname(xlrd.read_excel_two(10,1),xlrd.read_excel(13,5))
            # 输入设备ID
            print("输入设备ID")
            self.dr.send_keysname(xlrd.read_excel_two(11,1),xlrd.read_excel(14,5))
            time.sleep(1)
            # 点击保存
            print("点击保存")
            self.dr.Clickclass_last(xlrd.read_excel_two(12,1))
            print("搜索新添加的车位")
            time.sleep(4)
            # 在搜索框输入0001
            self.dr.send_keysid(xlrd.read_excel_two(13,1),xlrd.read_excel_two(13,1),xlrd.read_excel(13,5))
            # 点击查询
            self.dr.Clickid(xlrd.read_excel_two(14,1))
            # 断言
            time.sleep(5)
            print("开始断言")
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(4,1)),self.dr.Assert2(xlrd.read_excel_three(4,2)))
            print("用例成功")
        except Exception as msg:
            self.dr.getImage()
            logger.info("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_05(self):
        '''搜索后点击重置'''
        print("--------------用例5------------------")
        try:
            time.sleep(2)
            logging.info("点击重置")
            self.dr.Clickid(xlrd.read_excel_two(15,1))
            time.sleep(20)
            logging.info("开始断言")
            self.dr.is_login_sucess_chongzhi(xlrd.read_excel_three(5,1))
        except Exception as msg:
            self.dr.getImage()
            logger.info("异常原因%s"%msg)
            # raise抛出异常
            raise

    def test_06(self):
        '''车位导出'''
        print("--------------用例6------------------")
        try:
            time.sleep(5)
            print("点击导出")
            self.dr.Clickxpath(xlrd.read_excel_two(16,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(6,1))
            print("用例结束")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            print("用例失败")
            raise

    def test_07(self):
        '''下载车位模板'''
        print("--------------用例7------------------")
        try:
            time.sleep(5)
            print("点击下载车位模板")
            self.dr.Clickxpath(xlrd.read_excel_two(17,1))
            time.sleep(10)
            print("开始断言")
            self.dr.daochu(xlrd.read_excel_three(7,1))
            print("用例结束")
        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            print("用例失败")
            raise

    def test_08(self):
        '''车位导入'''
        print("--------------用例8------------------")
        try:
            time.sleep(5)
            print("点击导入")
            self.dr.Clickxpath(xlrd.read_excel_two(18,1))
            print("打开选择文件，导入文件")
            self.dr.send_keysdao(xlrd.read_excel_two(19,1),xlrd.read_excel(19,5))
            time.sleep(2)
            print("点击保存")
            self.dr.Clickid(xlrd.read_excel_two(21,1))
            time.sleep(5)
            self.dr.Clickxpath(xlrd.read_excel_two(22,1))
            time.sleep(5)
            print("开始断言")
            # 在搜索框输入3333
            self.dr.send_keysid(xlrd.read_excel_two(13,1),xlrd.read_excel_two(13,1),xlrd.read_excel(20,5))
            # 点击查询
            self.dr.Clickid(xlrd.read_excel_two(14,1))
            # 断言
            time.sleep(5)
            self.assertEqual(self.dr.Assert1(xlrd.read_excel_three(8,1)),self.dr.Assert2(xlrd.read_excel_three(8,2)))
            print("用例成功")

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            print("用例失败")
            raise

    def test_09(self):
        '''车位删除'''
        print("--------------用例9------------------")
        try:
            time.sleep(5)
            print("-----删除0001-----")
            # 在搜索框输入0001
            self.dr.send_keysid(xlrd.read_excel_two(13,1),xlrd.read_excel_two(13,1),xlrd.read_excel(13,5))
            print("点击查询")
            # 点击查询
            self.dr.Clickid(xlrd.read_excel_two(14,1))
            time.sleep(2)
            # 点击删除
            print("点击删除")
            self.dr.Clickxpath(xlrd.read_excel_two(20,1))
            time.sleep(1)
            print("点击弹窗确定")
            self.dr.Clickid(xlrd.read_excel_two(23,1))
            time.sleep(3)
            print("点击成功确定")
            self.dr.Clickxpath(xlrd.read_excel_two(24,1))
            time.sleep(3)

            print("-----删除3333-----")
            # 在搜索框输入3333
            self.dr.send_keysid(xlrd.read_excel_two(13,1),xlrd.read_excel_two(13,1),xlrd.read_excel(20,5))
            print("点击查询")
            # 点击查询
            self.dr.Clickid(xlrd.read_excel_two(14,1))
            time.sleep(2)
            # 点击删除
            print("点击删除")
            self.dr.Clickxpath(xlrd.read_excel_two(20,1))
            time.sleep(1)
            print("点击弹窗确定")
            self.dr.Clickid(xlrd.read_excel_two(23,1))
            time.sleep(3)
            print("点击成功确定")
            self.dr.Clickxpath(xlrd.read_excel_two(24,1))

        except Exception as msg:
            self.dr.getImage()
            print("异常原因%s"%msg)
            # raise抛出异常
            print("用例失败")
            raise




if __name__ == '__main__':
    unittest.main()
