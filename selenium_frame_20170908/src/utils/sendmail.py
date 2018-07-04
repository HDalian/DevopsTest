# coding: utf-8
'''
Created on 2017年9月12日

@author: zhanghui
'''

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
#from email.header import Header
from utils.config import REPORT_PATH
from utils.log import logger

sender = 'zhtlforever@163.com'
password = 'huiwenyuan011026'     #发件人邮箱开启并设置客户端授权密码
receiver = 'zhtlforever@163.com'


def mail():
    ret = True
    try:
        msg = MIMEMultipart()  #创建带附件的实例
        #msg = MIMEText('测试报告','plain','utf-8')  # msg，样式，编码（无附件）
        msg['From'] = formataddr(['FromHui',sender])
        msg['To'] = formataddr(['ToHui',receiver])
        msg['Subject'] = 'Test Report'             #标题
        
        # 添加附件1
        msg.attach(MIMEText('测试报告','plain','utf-8'))
        report = REPORT_PATH + '/report.html'
        att1 = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="testreport.html"'  #filename代表邮件中显示的名字
        msg.attach(att1)
        
        server = smtplib.SMTP_SSL('smtp.163.com', 465)  #发件人邮箱中的SMTP服务器，SSL协议端口号是465
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        
        server.quit()  #关闭连接
        logger.info('send mail'.format(sender, receiver))
    except Exception:
        ret = False
    return ret 
'''
ret = mail()
if ret:
    print '邮件发送成功'
else:
    print '邮件发送失败'
'''