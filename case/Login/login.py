"""后台登录"""

import time
from case.test_case.Auxiliary.auxiliary import Driver
from case.common.excel.xlrd import xlrd
import logging


#创建logger，如果参数为空则返回root logger
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)  #设置logger日志等级



class Login():
    def __init__(self,driver):
        self.driver = Driver(driver)

    def login(self):
        '''进入后台登录'''
        # 输入账号，读取excel文档内容
        self.driver.send_keysid(xlrd.read_excel_two(1,1),xlrd.read_excel_two(1,1),xlrd.read_excel(1,5))
        # 输入密码，读取excel文档内容
        self.driver.send_keysid(xlrd.read_excel_two(2,1),xlrd.read_excel_two(2,1),xlrd.read_excel(2,5))
        # 点击确定，读取excel文档内容
        self.driver.Clickid(xlrd.read_excel_two(3,1))





    def Parking_Management(self):
        '''进入车位管理'''
        # 进入停车场二代管理,读取excel文档内容
        print("点击停车场二代管理")
        self.driver.Clickxpath(xlrd.read_excel_two(4,1))
        time.sleep(10)
        # 悬停在停车场信息管理上,读取excel文档内容
        print("商标悬停在车位管理上")
        self.driver.Action(xlrd.read_excel_two(5,1))
        # 隐式等待30秒
        self.driver.impicitly()
        # 进入车位管理,读取excel文档内容
        print("点击车位管理")
        self.driver.Clickid(xlrd.read_excel_two(6,1))
        print("进入车位管理")
        time.sleep(5)
        # 选择停车场,读取excel文档内容
        self.driver.Clickid(xlrd.read_excel_two(7,1))
        print("已选择停车场")
        time.sleep(5)


    def Charge_Management(self):
        '''进入收费规则管理'''
        # 进入停车场二代管理,读取excel文档内容
        print("点击停车场二代管理")
        self.driver.Clickxpath(xlrd.read_excel_two(4,1))
        time.sleep(10)
        # 悬停在停车场信息管理上,读取excel文档内容
        print("商标悬停在收费规则管理上")
        self.driver.Action_xpath(xlrd.read_excel_two(25,1))
        self.driver.impicitly()
        # 进入车位管理,读取excel文档内容
        print("点击收费规则管理")
        self.driver.Clickxpath(xlrd.read_excel_two(26,1))
        print("进入收费规则管理")
        time.sleep(5)
        # 选择停车场,读取excel文档内容
        self.driver.Clickid(xlrd.read_excel_two(7,1))
        print("已选择停车场")
        time.sleep(5)


    def Vehicles_and_recharge(self):
        '''进入车辆与充值管理'''
        # 进入停车场二代管理,读取excel文档内容
        print("点击停车场二代管理")
        self.driver.Clickxpath(xlrd.read_excel_two(4,1))
        time.sleep(10)
        # 悬停在停车场信息管理上,读取excel文档内容
        print("商标悬停在车辆管理上")
        self.driver.Action_xpath(xlrd.read_excel_two(40,1))
        self.driver.impicitly()
        # 进入车位管理,读取excel文档内容
        print("点击车辆与充值管理")
        self.driver.Clickxpath(xlrd.read_excel_two(41,1))
        print("进入车辆与充值管理")
        time.sleep(5)
        # 选择停车场,读取excel文档内容
        self.driver.Clickid(xlrd.read_excel_two(7,1))
        print("已选择停车场")
        time.sleep(5)

    def Recharge_statistics(self):
        '''进入固定临停车充值统计'''
        # 悬停在停车场信息管理上,读取excel文档内容
        print("商标悬停在车辆管理上")
        self.driver.Action_xpath(xlrd.read_excel_two(40,1))
        self.driver.impicitly()
        # 进入固定临停车充值统计,读取excel文档内容
        print("点击固定临停车充值统计")
        self.driver.Clickxpath(xlrd.read_excel_two(70,1))
        print("进入固定临停车充值统计")
        time.sleep(5)
        # 选择物业,读取excel文档内容
        self.driver.Clickxpath(xlrd.read_excel_two(71,1))
        print("已选择物业")
        time.sleep(5)

    def System_settings(self):
        '''进入系统设置'''
        # 进入停车场二代管理,读取excel文档内容
        print("点击停车场二代管理")
        self.driver.Clickxpath(xlrd.read_excel_two(4,1))
        time.sleep(15)
        # 悬停在系统设置上,读取excel文档内容
        print("商标悬停在系统设置上")
        self.driver.Action_xpath(xlrd.read_excel_two(79,1))
        self.driver.impicitly()
        # 进入系统设置,读取excel文档内容
        print("点击系统设置")
        self.driver.Clickxpath(xlrd.read_excel_two(80,1))
        print("进入系统设置")
        time.sleep(5)
        # 选择物业,读取excel文档内容
        self.driver.Clickxpath(xlrd.read_excel_two(81,1))
        print("已选择系统设置")
        time.sleep(5)


    def Charge_statemen(self):
        '''进入收费报表'''
        # 进入停车场二代管理,读取excel文档内容
        print("点击停车场二代管理")
        self.driver.Clickxpath(xlrd.read_excel_two(4,1))
        time.sleep(15)
        # 悬停在报表信息上,读取excel文档内容
        print("商标悬停在报表信息上")
        self.driver.Action_xpath(xlrd.read_excel_two(120,1))
        self.driver.impicitly()
        # 进入收费报表,读取excel文档内容
        print("点击收费报表")
        self.driver.Clickxpath(xlrd.read_excel_two(121,1))
        print("进入收费报表")
        time.sleep(5)
        # 选择停车场,读取excel文档内容
        self.driver.Clickid(xlrd.read_excel_two(7,1))
        print("已选择收费报表")
        time.sleep(5)


    def Vehicle_Passing_record(self):
        '''进入过车记录查询'''
        # 进入停车场二代管理,读取excel文档内容
        print("点击停车场二代管理")
        self.driver.Clickxpath(xlrd.read_excel_two(4,1))
        time.sleep(15)
        # 悬停在报表信息上,读取excel文档内容
        print("商标悬停在报表信息上")
        self.driver.Action_xpath(xlrd.read_excel_two(120,1))
        self.driver.impicitly()
        # 进入过车记录查询,读取excel文档内容
        print("点击过车记录查询")
        self.driver.Clickxpath(xlrd.read_excel_two(132,1))
        print("进入过车记录查询")
        time.sleep(5)
        # 选择停车场,读取excel文档内容
        self.driver.Clickid(xlrd.read_excel_two(7,1))
        print("已选择过车记录")
        time.sleep(5)
