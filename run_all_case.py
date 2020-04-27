# coding:utf-8
# 最终运行文件
import os
import sys
sys.path.append('E:\\huangye')
import unittest
from case.common import HTMLtestRunner
import time
from case.common.Email.yagmail import HTMLemail
from case.common.Zipfile.zipfile import zip_file_path
from case.common.Delete import delete


# 用例路径
case_path = os.path.join(os.getcwd(),"E:\\huangye\\case\\test_case\\test")
# 报告存放路径
report_path = os.path.join(os.getcwd(),"E:\\huangye\\case\\report\\report")

'''执行所有test的用例'''
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    # html报告文件路径
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    report_abspath = os.path.join(report_path, "UI自动化测试报告-%s.html" %nowTime)
    fp = open(report_abspath, "wb")

    runner = HTMLtestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：',
                                           verbosity=2
                                           )

    # 调用add_case函数返回值
    #运行用例
    runner.run(all_case())
    # 生成报告
    fp.close()
    # 打包测试报告
    zip_file_path(r"E:\\huangye\\case\\report\\report\\", 'E:\\huangye\\case\\report\\', 'UI自动化测试报告包-%s.zip' %nowTime)
    # 发邮件
    HTMLemail()
    time.sleep(2)

    delete.deleteZIP()
    delete.deleteHTML()
    delete.deletePNG()













