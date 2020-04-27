import yagmail
import os
'''Email邮件'''
def HTMLemail():
    report_dir = "E:\\huangye\\case\\report\\"
    lists = os.listdir((report_dir))
    lists.sort(key= lambda filename : os.path.getatime(report_dir + filename))
    recent = lists[-1]
    file = os.path.join(report_dir,recent)

    # 填写登录信息
    yag = yagmail.SMTP(user= "hyxyuxiao@163.com",password="910525123",host="smtp.163.com")
    # 邮件正文
    content = "云端测试报告"
    # 将测试报告作为附件发送
    yag.send(["huangyuxiao@yun-kai.com","tangting@yun-kai.com"],"测试报告",content,file)
    #yag.send("huangyuxiao@yun-kai.com","测试报告",content,file)

