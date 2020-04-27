"""selnium底层辅助功能"""

import os,sys,logging
import time
from selenium.webdriver.common.action_chains import ActionChains
import logging
import os
from selenium.webdriver.common.keys import Keys

#创建logger，如果参数为空则返回root logger
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)  #设置logger日志等级


class Driver():

    # 构建driver方法
    def __init__(self,driver):
        self.driver = driver

    # 打开网页
    def open_url(self,url):
        self.driver.get(url)

    # 关闭浏览器
    def quit_web(self):
        self.driver.quit()

    # 鼠标悬停XX上 id
    def  Action(self,ele):
         # 悬停
        mouse = self.driver.find_element_by_id(ele)
        print("鼠标悬停")
        ActionChains(self.driver).move_to_element(mouse).perform() # perform（）执行所有ActionChains中的行为

    # 鼠标悬停XX上 xpath
    def  Action_xpath(self,ele):
         # 悬停
        mouse = self.driver.find_element_by_xpath(ele)
        print("鼠标悬停")
        ActionChains(self.driver).move_to_element(mouse).perform() # perform（）执行所有ActionChains中的行为

    # 定位xpath输入
    def send_keys(self,element,elementxpath,input):
        # 清空输入框
        self.driver.find_element_by_xpath(element).clear()
        # 输入内容
        self.driver.find_element_by_xpath(elementxpath).send_keys(input)


    # 定位id输入
    def send_keysid(self,element,elementid,input):
        # 清空输入框
        self.driver.find_element_by_id(element).clear()
        # 输入内容
        self.driver.find_element_by_id(elementid).send_keys(input)

    # 定位class输入
    def send_keysclass(self,element,input):
        # 清空输入框
        self.driver.find_element_by_class_name(element).clear()
        # 输入内容
        self.driver.find_element_by_class_name(element).send_keys(input)

    # 定位name输入
    def send_keysname(self,element,input):
        # 清空输入框
        self.driver.find_element_by_name(element).clear()
        # 输入内容
        self.driver.find_element_by_name(element).send_keys(input)

    # 导入用的xpath输入
    def send_keysdao(self,elementxpath,input):
        # 输入内容
        self.driver.find_element_by_xpath(elementxpath).send_keys(input)

    # 导入用的class输入
    def send_keysdaoru(self,elementxpath,input):
        # 输入内容
        self.driver.find_element_by_class_name(elementxpath).send_keys(input)


    # 定位id点击
    def Clickid(self,cl):
        self.driver.find_element_by_id(cl).click()


    # 定位xpath点击
    def Clickxpath(self,cl):
        self.driver.find_element_by_xpath(cl).click()

    # 定位class点击
    def Clickclass(self,cl):
        self.driver.find_element_by_class_name(cl).click()


    # 定位xpath最后一个元素点击
    def Clickxpath_last(self,cl):
        # 同一个界面遇到两个相同的元素，就使用这个点击方法
        self.driver.find_elements_by_xpath(cl)[1].click()

    # 定位class最后一个元素点击
    def Clickclass_last(self,cl):
        # 同一个界面遇到两个相同的元素，就使用这个点击方法
        self.driver.find_elements_by_class_name(cl)[9].click()



    # 复选框定位xpath点击
    def Clickxpath_select(self,cl):
        s = self.driver.find_element_by_xpath(cl).is_selected()
        print("目前复选框状态为：",s)
        if s == False:
            print("复选框没有被点击，点击")
            self.driver.find_element_by_xpath(cl).click()
            r = self.driver.find_element_by_xpath(cl).is_selected()
            print("目前复选框状态为：",r)
            time.sleep(1)
        else:
            print("复选框已经勾选，不用勾选了")
            time.sleep(1)

    # 下拉菜单选择
    def drop_down(self,s1,s2):
        # 定位下拉菜单框
        select1 = self.driver.find_element_by_xpath(s1)
        # 选择下拉菜单框内的元素
        select1.find_element_by_xpath(s2).click()


    # 隐式等待
    def impicitly(self):
        self.driver.implicitly_wait(30)

    # 获取登录文本，判断正确
    def is_login_sucess(self,user_element):
        """获取登录的文本"""
        t = self.driver.find_element_by_xpath(user_element).text
        print("获取参数：%s" %t)
        if t == "用户名或密码错误":
            logger.info("登录失败")
            logger.info("用例成功")
        else:
            logger.info("登陆成功")
            logger.info("用例失败")
            # raise抛出异常
            raise

       # 获取重置后的页数文本，判断正确
    def is_login_sucess_chongzhi(self,user_element):
        """获取登录的文本"""
        t = self.driver.find_element_by_id(user_element).text
        print("获取参数：%s" %t)
        if "显示第 1 至 9 项结果" in t:
            logger.info("数据一致")
            logger.info("用例成功")
        else:
            logger.info("数据不一致")
            logger.info("用例失败")
            # raise抛出异常
            raise

    # 获取重置后的页数文本，判断正确
    def text_duanyan(self,user_element,text):
        """获取登录的文本"""
        t = self.driver.find_element_by_xpath(user_element).text
        print("获取参数：%s" %t)
        if t == text:
            print("数据一致")
            print("用例成功")
        else:
            print("数据不一致")
            print("用例失败")
            # raise抛出异常
            raise

    # 断言
    def Assert1(self,text):
        t = self.driver.find_element_by_xpath(text).text
        logger.info("第一个文本：%s" %t)
    def Assert2(self,text2):
        d = self.driver.find_element_by_xpath(text2).text
        logger.info("第二个文本：%s" %d)




    def getImage(self):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        self.timestrmap = time.strftime('%Y%m%d.%H.%M.%S')
        imgPath = os.path.join("E:\\huangye\\case\\report\\report\\images", '%s.png' % str(self.timestrmap))
        self.driver.save_screenshot(imgPath)
        print('screenshot:', self.timestrmap, '.png')


    def daochu(self,text):
        '''导出断言'''
        # 需要把路径替换成你的文件夹所在路径
        path = 'C:/Users/ChenYang/Downloads/'
        # 利用os模块中的listdir函数和for语句，浏览所有文件
        files = os.listdir(path)
        for f in files:
            # 判断文件是否符合要求
            if(f.endswith('.xls') and (text) in f):
                # 如果符合要求，则输出文件名
                print("xls文件名：%s" %f)
                if text in f:
                    print("导出成功")
                    print("用例成功")
                    print("删除文件")
                    os.remove('C:/Users/ChenYang/Downloads/%s'% f)
                    print("删除成功")

                else:
                    print("没找到文件，用例失败")
                    # raise抛出异常
                    raise


    def daochu_xlsx(self,text):
        '''导出xlsx断言'''
        # 需要把路径替换成你的文件夹所在路径
        path = 'C:/Users/ChenYang/Downloads/'
        # 利用os模块中的listdir函数和for语句，浏览所有文件
        files = os.listdir(path)
        for f in files:
            # 判断文件是否符合要求
            if(f.endswith('.xlsx') and (text) in f):
                # 如果符合要求，则输出文件名
                print("xlsx文件名：%s" %f)
                if text in f:
                    print("导出成功")
                    print("用例成功")
                    print("删除文件")
                    os.remove('C:/Users/ChenYang/Downloads/%s'% f)
                    print("删除成功")

                else:
                    print("没找到文件，用例失败")
                    # raise抛出异常
                    raise



    def is_element_exist(self,xpath):
        flag = self.driver.find_element_by_id(xpath)
        if len(flag) == 0:
            print( "元素未找到:%s"% xpath)
            return False
        elif len(flag) == 1:
            return True
