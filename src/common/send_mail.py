# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# def send_email(file):
#
#     sender="zhangman@youliang100.com"
#     user="zhangman@youliang100.com"
#     pwd='yl123456!'
#     receiver="zhangman@youliang100.com"
#     smtpserver="smtp.youliang100.com"
#     subject="优粮自动化测试报告"
#     f=open(file,'rb')
#     fp=f.read()
#     f.close()
#
#     msg=MIMEText(fp,'html','utf-8')
#     msg['subject']=Header(subject,'utf-8')
#     #展示出发件人和收件人
#     msg['From'] = Header('张蔓<zhangman@youlaing100.com>','utf-8')     #这样发件人那里显示的是张蔓<zhangman@youlaing100.com>
#     msg['To'] = Header('张蔓','utf-8')                         #这样写，收件人那里写的是张蔓<张蔓>
#
#     smtp=smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(user,pwd)
#     smtp.sendmail(sender,receiver,msg.as_string())
#     smtp.quit()
# send_email("C:\\Users\\Alex\\PycharmProjects\\untitled\\youliang\\report\\2018_03_01_15_38_12report.html")

# #虫师的方法，但是发送的附件展示了所有用例的执行日志，很乱，且发件人和收件人是空
# #带附件发送邮件
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# from email.utils import parseaddr,formataddr
#
# def send_email(file):
#     #格式化邮件地址
#     def _format_addr(s):
#         name, addr = parseaddr(s)
#         return formataddr((Header(name, 'utf-8').encode(), addr))
#     # 发送邮箱服务器
#     smtpserver = 'smtp.youliang100.com'
#     # 发送邮箱
#     sender = 'zhangman@youliang100.com'
#     # 接收邮箱
#     receiver = 'zhangman@youliang100.com'
#     # 发送邮箱用户/密码
#     user = 'zhangman@youliang100.com'
#     password = 'yl123456!'
#     # 邮件主题
#     subject = '自动化测试报告'
#     # 发送的附件
#     sendfile = open(file,'rb').read()
#     att = MIMEText(sendfile, 'base64','utf-8')
#     att["Content-Type"] = 'application/octet-stream'
#     fn=file.split("/")[-1]
#     #att["Content-Disposition"] = 'attachment; filename=fn'
#     #以上的方式来设置附件文件名，不行，filename=后边的是按字符串处理的，发送后的附件名为fn
#     att["Content-Disposition"] = 'attachment; filename='+fn
#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = subject
#     #展示出发件人和收件人
#     msgRoot['From'] = _format_addr(u'测试猿<%s>' % sender)
#     msgRoot['To'] = _format_addr(u'管理员 <%s>' % receiver)
#
#     msgRoot.attach(att)
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(user, password)
#     smtp.sendmail(sender, receiver, msgRoot.as_string())
#     smtp.quit()
#
# send_email("C:\\Users\\Alex\\PycharmProjects\\untitled\\youliang\\report\\2018_03_01_15_38_12report.html")

#廖雪峰的发附件方法
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
def send_mail(fp):
    #格式化邮件地址
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    sender="zhangman@youliang100.com"
    user="zhangman@youliang100.com"
    pwd='yl123456!'
    receiver="zhangman@youliang100.com"
    smtpserver="smtp.youliang100.com"


    # 邮件对象
    msg = MIMEMultipart()
    msg['From'] = _format_addr(u'测试猿<%s>' % sender)
    msg['To'] = _format_addr(u'管理员 <%s>' % receiver)
    msg['Subject'] = Header(u'优粮自动化测试报告','utf-8')

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('hello ,send by Python ....', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase 从本地读取一个文件
    # fn = fp.split("/")[-1]   # 获取要发送文件的名称
    fn=os.path.basename(fp)   # os.path.basename(path):返回path最后的文件名。如果path以／或\结尾，那么就会返回空值
    with open(fp, 'rb') as f:
        # 附件用MIMEBase
        # 设置附件的MIME和文件名
        mime = MIMEBase('application','octet-stream', filename=fn)
        # 加上必要的MIME头信息
        mime.add_header('Content-Disposition', 'attachment', filename=fn)

        # 把附件内容读进来
        mime.set_payload(f.read())
        # 利用base64编码
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    server = smtplib.SMTP(smtpserver, 25)
    # server.set_debuglevel(1)   #显示邮件发送日志
    server.login(user, pwd)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()

# send_mail("C:\\Users\\Alex\\PycharmProjects\\untitled\\youliang\\report\\2018_03_01_15_38_12report.html")
