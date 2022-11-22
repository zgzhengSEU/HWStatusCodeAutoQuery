import sys
import time
import os
import requests
from datetime import datetime
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendEmail(email, passwd, host_server):
    sender_qq = email
    pwd = passwd
    receiver = [email]
    mail_title = '华为状态码变了！！！'
    mail_content = "iv_date提前了"
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    msg['To'] = ";".join(receiver)
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    smtp = SMTP_SSL(host_server)
    smtp.login(sender_qq, pwd)
    smtp.sendmail(sender_qq, receiver, msg.as_string())
    smtp.quit()


def sendEmailStart(email, passwd, host_server):
    sender_qq = email
    pwd = passwd
    receiver = [email]
    mail_title = '今日华为状态码脚本启动成功，正在运行中，早日offer！'
    mail_content = "今日华为状态码脚本启动成功，正在运行中，早日offer！"
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    msg['To'] = ";".join(receiver)
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    smtp = SMTP_SSL(host_server)
    smtp.login(sender_qq, pwd)
    smtp.sendmail(sender_qq, receiver, msg.as_string())
    smtp.quit()


def queryStatus(hwuid, password, email, passwd, host_server, deviceFingerInfo):
    session = requests.session()
    data = {'uid': hwuid,
            'password': password,
            'actionFlag': 'loginAuthenticate',
            'lang': 'zh_CN',
            'redirect': 'https%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Flogin_index.html%3Fredirect%3Dhttps%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Fportal5%2Findex.html%3Fi%3D83760',
            'loginFlag': 'byUid',
            'deviceFingerInfo': deviceFingerInfo,
            'redirect_local': '',
            'redirect_modify': '',
            'getloginMethod': 'null',
            'selectedAccount': ''}
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    login_url = 'https://uniportal.huawei.com/uniportal/login.do'
    r = session.post(login_url, headers=headers, data=data, timeout=5)
    cur_time = datetime.now().timestamp()
    print('\n 当前时间为：' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time = int(cur_time * 1000)
    url = 'https://career.huawei.com/reccampportal/services/portal/portaluser/queryMyJobInterviewPortal5?reqTime='
    url = url + str(time)
    html_src = session.get(url, timeout=5, headers=headers)
    logout_url = 'https://uniportal.huawei.com/uniportal/logout.do?redirect=http://career.huawei.com/reccampportal/&lang=zh'
    session.get(logout_url, timeout=5, headers=headers)  # 新增退出登录逻辑
    res = html_src.content.decode('utf-8')
    res_list = res.split('{')[1][:-2].split(',')
    print("当前状态码为：\n")
    for res in res_list:
        print(res)
    print()
    if res_list[0].split(':')[0] == '"IV_DATE"':
        sendEmail(email, passwd, host_server)
        print("状态码变了！")
        return True
    else:
        print("继续爱信等！")
    print()
    return False


def work(hwuid, password, your_email, email_password, host_server, start_time, deviceFingerInfo):
    try:
        while True:
            if (datetime.now() - start_time).seconds > 18000:
                break
            if queryStatus(hwuid, password, your_email, email_password, host_server, deviceFingerInfo):
                break
            time.sleep(queryInterval)
    except:
        work(hwuid, password, your_email, email_password, host_server, start_time, deviceFingerInfo)

        
if __name__ == "__main__":
    if "HWUID" in os.environ:
        hwuid = os.environ["HWUID"]
        if hwuid == '':
            print("[", datetime.now(), "] ", "未找到 HWUID ！")
            sys.exit(1) 
    else:
        print("[", datetime.now(), "] ", "未找到 HWUID ！")
        sys.exit(1)

    if "PASSWORD" in os.environ:
        password = os.environ["PASSWORD"]
        if password == '':
            print("[", datetime.now(), "] ", "未找到 PASSWORD ！")
            sys.exit(1) 
    else:
        print("[", datetime.now(), "] ", "未找到 PASSWORD ！")
        sys.exit(1)

    if "EMAIL" in os.environ:
        your_email = os.environ["EMAIL"]
        if your_email == '':
            print("[", datetime.now(), "] ", "未找到 EMAIL ！")
            sys.exit(1) 
    else:
        print("[", datetime.now(), "] ", "未找到 EMAIL ！")
        sys.exit(1)

    if "EMAILCODE" in os.environ:
        email_password = os.environ["EMAILCODE"]
        if email_password == '':
            print("[", datetime.now(), "] ", "未找到 EMAILCODE ！")
            sys.exit(1) 
    else:
        print("[", datetime.now(), "] ", "未找到 EMAILCODE ！")
        sys.exit(1)

    if "SMTP" in os.environ:
        host_server = os.environ["SMTP"]
        if host_server == '':
            print("[", datetime.now(), "] ", "未填写SMTP，默认使用QQ邮箱，SMTP 服务器为 smtp.qq.com")
            host_server = 'smtp.qq.com'            
        else:
            print("[", datetime.now(), "] ", "设置 SMTP 服务器为：", host_server)
    else:
        print("[", datetime.now(), "] ", "未填写SMTP，默认使用QQ邮箱，SMTP 服务器为 smtp.qq.com")
        host_server = 'smtp.qq.com'

    if "NOTIFY" in os.environ:
        notify = os.environ["NOTIFY"]
        if notify.lower() == "false":
            notify = False
            print("[", datetime.now(), "] ", "关闭功能：每日定时启动脚本时，发送提醒脚本运行成功邮件")
        else:
            notify = True
            print("[", datetime.now(), "] ", "开启功能：每日定时启动脚本时，发送提醒脚本运行成功邮件")
    else:
        notify = True
        print("[", datetime.now(), "] ", "开启功能：每日定时启动脚本时，发送提醒脚本运行成功邮件")
    
    if "DFI" in os.environ:
        deviceFingerInfo = os.environ["DFI"]
        if deviceFingerInfo == '':
            print("[", datetime.now(), "] ", "请填写deviceFingerInfo，否则请检测是否运行成功，可能会出错")
            deviceFingerInfo = 'bb84ac09e32b0ce23d488372c91a81d6'
    else:
        print("[", datetime.now(), "] ", "请填写deviceFingerInfo，否则请检测是否运行成功，可能会出错")
        deviceFingerInfo = 'bb84ac09e32b0ce23d488372c91a81d6'
    
    if len(sys.argv) == 2 and sys.argv[1] == 'test': # 添加快速测试
        print("[", datetime.now(), "] ", "开始运行测试job")
        queryStatus(hwuid, password, your_email, email_password, host_server, deviceFingerInfo)
        print("[", datetime.now(), "] ", "测试job结束，开始进入正式运行")
        sys.exit(0)
    
    if notify:
        # 每天脚本定时运行时，发送启动成功提醒
        if len(sys.argv) == 2 and sys.argv[1] == 'start':
            print("[", datetime.now(), "] ", "发送 每天脚本定时运行成功提醒")
            sendEmailStart(your_email, email_password, host_server)

    queryInterval = 1800  # 默认半小时查询一次
    start_time = datetime.now()
    print("[", start_time, "] ", "启动当前job")

    work(hwuid, password, your_email, email_password, host_server, start_time, deviceFingerInfo)

    print("[", datetime.now(), "] ", "当前job成功运行5小时，切换下一个job")
