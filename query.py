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


def queryStatus(uid, password, email, passwd, host_server):
    session = requests.session()
    data = {'uid': uid,
            'password': password,
            'actionFlag': 'loginAuthenticate',
            'lang': 'en_US',
            'redirect': 'https%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Flogin_index.html%3Fredirect%3Dhttps%3A%2F'
                        '%2Fcareer.huawei.com%2Freccampportal%2Fportal5%2Findex.html%3Fi%3D78302',
            'loginFlag': 'byUid',
            'deviceFingerInfo': 'd36a786626c0c6417af75105301d425b',
            'redirect_local': '',
            'redirect_modify': '',
            'getloginMethod': 'null',
            'selectedAccount': ''}
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    login_url = 'https://uniportal.huawei.com/uniportal/login.do'
    r = session.post(login_url, headers=headers, data=data, timeout=5)
    cur_time = datetime.now().timestamp()
    print('当前时间为' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time = int(cur_time * 1000)
    url = 'https://career.huawei.com/reccampportal/services/portal/portaluser/queryMyJobInterviewPortal5?reqTime='
    url = url + str(time)
    html_src = session.get(url, timeout=5, headers=headers)
    res = html_src.content.decode('utf-8')
    res_list = res.split('{')[1][:-2].split(',')

    if res_list[0].split(':')[0] == '"IV_DATE"':
        sendEmail(email, passwd, host_server)
        sys.exit()
    for res in res_list:
        print(res)
    print()


if __name__ == "__main__":
    if "UID" in os.environ:
        uid = os.environ["UID"]
    else:
        print("未找到 UID")
        # sys.exit(1)

    if "HWUID" in os.environ:
        uid = os.environ["HWUID"]
    else:
        print("未找到 HWUID")
        # sys.exit(1)

    if "PASSWORD" in os.environ:
        password = os.environ["PASSWORD"]
    else:
        print("未找到 PASSWORD")
        sys.exit(1)

    if "EMAIL" in os.environ:
        your_email = os.environ["EMAIL"]
    else:
        print("未找到 EMAIL")
        sys.exit(1)

    if "EMAILCODE" in os.environ:
        email_password = os.environ["EMAILCODE"]
    else:
        print("未找到 EMAILCODE！")
        sys.exit(1)

    if "STMP" in os.environ:
        host_server = os.environ["STMP"]
    else:
        host_server = 'smtp.qq.com'

    if "NOTIFY" in os.environ:
        notify = os.environ["NOTIFY"]
        if notify.lower() == "true":
            notify = True
        else:
            notify = False
    else:
        notify = True

    if notify:
        # 每天脚本定时运行时，发送启动成功提醒
        sendEmailStart(your_email, email_password, host_server)

    queryInterval = 1800  # 默认半小时查询一次
    start_time = datetime.now()
    print("[", start_time, "] ", "启动当前job")
    try:
        while True:
            if (datetime.now() - start_time).seconds > 20000:
                break
            queryStatus(uid, password, your_email, email_password, host_server)
            time.sleep(queryInterval)
    except:
        print('出错了请关闭梯子后重新运行')

    print("[", datetime.now(), "] ", "当前job成功运行6小时，切换下一个job")
