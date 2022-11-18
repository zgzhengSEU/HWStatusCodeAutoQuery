# 华为状态码自动查询工具
**华为状态码自动查询工具，利用 Github Action 全天候24h后台监测状态码，爱信等 ALL IN 起来 ！！！**
**状态码变了后会发邮件到设定的邮箱！**

![Stars](https://img.shields.io/github/stars/zgzhengSEU/HWStatusCodeAutoQuery.svg)
![Forks](https://img.shields.io/github/forks/zgzhengSEU/HWStatusCodeAutoQuery.svg)

有问题提Issues

## 使用步骤

### 1 右上角点个小星星⭐ fork 脚本到自己的仓库~
  
![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211111311139.png)

### 2 进入自己 fork 的仓库，进入 Actions 并 Enable Workflow

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211102359648.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110000533.png)

### 3 进入自己 fork 的仓库，点击 Settings -> Secrets -> New repository secret，添加下列Secret供脚本使用。

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110006864.png)

![image](https://user-images.githubusercontent.com/62554593/201380696-b589a2a7-223a-4d69-a98f-4bc1555cc790.png)![image](https://user-images.githubusercontent.com/62554593/201381403-f8581552-c8ad-4320-8c15-20dacae78dbd.png)![image](https://user-images.githubusercontent.com/62554593/201381505-e59bad75-c4d3-4951-bad3-4ae433df4b12.png)![image](https://user-images.githubusercontent.com/62554593/201381681-15725535-18bd-415c-adb5-2f801989df45.png)

**必须填写下面所有的secret**

| Secret     |可选性 | 解释                                                                           |
| ---------- |------| ------------------------------------------------------------                    |
| HWUID      | 必填 | 用户名，登录华为官网的账号                                                       |
| PASSWORD   | 必填 | 密码，登录华为官网的账号密码                                                      |
| EMAIL      | 必填 | 邮箱地址                                                                          |
| EMAILCODE  | 必填 | 邮箱密码/授权码。有的邮箱安全设置要求用授权码，如QQ邮箱。没有授权码要求的可以直接用邮箱密码 |
| SMTP       | 选填 | 不填则默认使用QQ邮箱。使用其他邮箱需要设置，如smtp.163.com、smtp.seu.edu.cn, 一般为stmp.邮箱域名 |
| NOTIFY     | 选填 | 不填默认开启每日通知。每日定时启动脚本时，是否发送提醒脚本运行成功邮件。填true/false。  |


[QQ邮件授权码设置教程,其他邮箱类似](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)。设置-> 账户->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

![056V7DNYS8VR$DK~R{MWCT7](https://user-images.githubusercontent.com/62554593/201148676-796927c2-2e98-4208-8763-ca5bbefbf902.png)

![2)OEIE9}$Z06DOF} W 8BAV](https://user-images.githubusercontent.com/62554593/201148533-27fb2038-8588-49de-97b0-dac2f86d9565.png)


### 4 给自己的仓库点star，可以手动启动脚本。脚本也会每天定时启动

启动后可以点进运行的workflow看看运行状态，如果出错，会报错误信息

![{51 2A2{7G8{OSQ`E2$0(UP](https://user-images.githubusercontent.com/62554593/201295883-efe0d151-c1ff-4664-88cb-9e38ce1b65a3.png)

![U)1MB50T RE%RJM7PZCIANV](https://user-images.githubusercontent.com/62554593/201296693-c84aecce-c527-447c-8ba0-6e51580547c6.png)

![image](https://user-images.githubusercontent.com/62554593/201296761-85cd60af-7e72-4311-85e1-d0f2ac985600.png)

workflow运行完成：
![image](https://user-images.githubusercontent.com/62554593/201655891-34e20847-883b-4cbb-808a-cadc97d7643f.png)

运行出错，可查看具体错误信息，如没设置好邮箱授权码：
![image](https://user-images.githubusercontent.com/62554593/201655792-7991f696-dd24-4043-ac8e-c08d5085552f.png)


### 参考

[@xyllq999](https://github.com/xyllq999/HwStatusCode)

[华为状态码轮询脚本（说不定查着查着就变了）](https://www.nowcoder.com/discuss/1093196?channel=-1&source_id=discuss_terminal_discuss_history_nctrack&ncTraceId=0efae7191ce247278d93842b70441cc5.1009.16682407933417590)
