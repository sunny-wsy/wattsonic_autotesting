# encoding='utf-8'
import sys,os
# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# sys_path = os.path.abspath(os.curdir)
#将工程目录添加到sys.path中
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sys_path)
import pytest,re
from email.mime.text import MIMEText
from email.message  import EmailMessage
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from API_autotesting.CommonModules import yaml_util
yaml_read=yaml_util.YamlUtil()
path='/data.yaml'

# sys.setdefaultencoding('utf8')
# 分3个步骤
# 第一步执行用例
# 第二步获取最新测试报告
# 第三步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）
def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file
#发送邮件配置
def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    # 定义邮件内容
    #定义邮件的内容为报告内容
    msg = MIMEMultipart()
    scene_body='附件为WattDesk接口自动化测试报告，请查收!<br>' \
               '<b>test_001_register</b>:注册相关接口<br>' \
               '<b>test_002_login</b>:登录相关接口<br>' \
               '<b>test_003_home</b>:首页相关接口<br>' \
               # '<b>test004</b>:数据查询相关接口<br>'
    f=open(report_file,'rb')
    mail_body=f.read()
    # print(mail_body)
    f.close()
    #将bytes类型转换为string
    #有中文的话，需要用下面的gbk,否则会报错。
    mail_body2=mail_body.decode('utf-8')
    # mail_body2=mail_body.decode('gbk')
    # print (mail_body2)
    #截取两个字符之间的字符串
    style=re.search('(<style>)(.*)(</style>)',mail_body2, re.S).group(2)
    style2='<style>'+style+'</style>'
    summary=re.search('(<h2>Summary</h2>)(.*)(<h2>Results</h2>)',mail_body2, re.S).group(2)
    tests_num=re.search('(<p>)(.*)(tests)',summary, re.S).group(2)
    failed_num=re.search('(class="failed">)(.*)(failed</span>)',summary, re.S).group(2)
    summary2='<h2>Summary</h2>'+summary+'<br>'+'<br>'
    mybody=style2+summary2+scene_body
    body = MIMEText(mybody, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"+'('+tests_num+'tests'+','+failed_num+'failed'+')'
    msg["from"] = sender
    # msg["to"] = receiver
    # 发现MIMEText()["to"]的数据类型与sendmail(from_addrs,to_addrs,...)的to_addrs不同；前者为str类型，多个地址使用逗号分隔，后者为list类型。
    msg["to"] = ','.join(receiver) if isinstance(receiver,list) else receiver
    # msg["to"] = ",".join(['liyanyan@maxtropy.com','liyanyan8759@163.com'])
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    if not isinstance(receiver,list):
        receiver=receiver.split(",")
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')
if __name__ == "__main__":
    #报告
    root_file=cur_path+'/report/report.html'
    # print(root_file)
    #用例路径
    case_file=cur_path+'/Auto_case'
    # print (case_file)
    # pytest.main(['--html=./report/report.html',"--self-contained-html"])
    #执行用例
    pytest.main(['%s'%case_file,'--html=%s'%root_file,"--self-contained-html"])
    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")  # 用例文件夹
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    #邮箱信息获取
    sender =yaml_read.read_test_yaml(path)['email']['sender']
    psw = yaml_read.read_test_yaml(path)['email']['psw']
    smtp_server = yaml_read.read_test_yaml(path)['email']['smtp_server']
    port = yaml_read.read_test_yaml(path)['email']['port']
    receiver = yaml_read.read_test_yaml(path)['email']['receiver']
    # receiver2=[]
    # receiver2.append(receiver)
    # 最后一步发送报告
    send_mail(sender, psw, receiver, smtp_server, report_file, port)