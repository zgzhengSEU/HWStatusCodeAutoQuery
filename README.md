# 华为状态码自动查询工具
**华为状态码自动查询工具，利用 Github Action 后台全天候24h监测状态码，爱信等 ALL IN 起来 ！！！**
**状态码变了后会发邮件到设定的邮箱！**

![Stars](https://img.shields.io/github/stars/zgzhengSEU/HWStatusCodeAutoQuery.svg)
![Forks](https://img.shields.io/github/forks/zgzhengSEU/HWStatusCodeAutoQuery.svg)

## 使用步骤

### 1 右上角点个小星星⭐ fork 脚本到自己的仓库~
  
![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211111311139.png)

### 2 进入自己 fork 的仓库，进入 Actions 并 Enable Workflow

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211102359648.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110000533.png)

### 3 进入自己 fork 的仓库，点击 Settings -> Secrets -> New repository secret，添加下列Secret供脚本使用。

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110006864.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211111323769.png)

**必须填写下面所有的secret**

| Secret     |可选性 | 解释                                                                           |
| ---------- |------| ------------------------------------------------------------                    |
| UID        | 必填 | 用户名，登录华为官网的账号                                                       |
| PASSWORD   | 必填 | 密码，登录华为官网的账号密码                                                      |
| EMAIL      | 必填 | 邮箱地址                                                                          |
| EMAILCODE  | 必填 | 邮箱密码/授权码                                                                   |
| STMP       | 选填 | 如果使用QQ邮箱，可不设置该项。使用其他邮箱需要设置，如stmp.163.com                 |
| NOTIFY     | 选填 | 每日定时启动脚本，是否发送提醒脚本运行成功邮件。填true/false。不填默认开启每日通知  |

![C_SO~T93~~~Y5 L7OJS6 PH](https://user-images.githubusercontent.com/62554593/201273620-1e57d6ea-3f11-48f0-b08b-0efd6ea9c3a2.png)

[QQ邮件授权码设置教程,其他邮箱类似](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)。设置-> 账户->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

![056V7DNYS8VR$DK~R{MWCT7](https://user-images.githubusercontent.com/62554593/201148676-796927c2-2e98-4208-8763-ca5bbefbf902.png)

![2)OEIE9}$Z06DOF} W 8BAV](https://user-images.githubusercontent.com/62554593/201148533-27fb2038-8588-49de-97b0-dac2f86d9565.png)


### 4 给自己的仓库点star，可以手动启动脚本。脚本也会每天定时启动

启动后可以点进运行的workflow看看运行状态，如果出错，会报错误信息

![{51 2A2{7G8{OSQ`E2$0(UP](https://user-images.githubusercontent.com/62554593/201295883-efe0d151-c1ff-4664-88cb-9e38ce1b65a3.png)

![U)1MB50T RE%RJM7PZCIANV](https://user-images.githubusercontent.com/62554593/201296693-c84aecce-c527-447c-8ba0-6e51580547c6.png)

![image](https://user-images.githubusercontent.com/62554593/201296761-85cd60af-7e72-4311-85e1-d0f2ac985600.png)


