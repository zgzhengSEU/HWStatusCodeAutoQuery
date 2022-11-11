# 华为状态码自动查询工具
**华为状态码自动查询工具，利用 Github Action 后台全天候24h监测状态码，爱信等 ALL IN 起来 ！！！**
**状态码变了后会发邮件到设定的邮箱！**

![Stars](https://img.shields.io/github/stars/zgzhengSEU/HWStatusCodeAutoQuery.svg)
![Forks](https://img.shields.io/github/forks/zgzhengSEU/HWStatusCodeAutoQuery.svg)

## 使用步骤

### 1 点个小星星⭐ fork 脚本到自己的仓库~
  
![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211111311139.png)

### 2 进入自己 fork 的仓库，进入 Actions 并 Enable Workflow

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211102359648.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110000533.png)

### 3 进入自己 fork 的仓库，点击 Settings -> Secrets -> New repository secret，添加下列Secret供脚本使用。

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110006864.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211111323769.png)

**必须填写下面所有的secret**

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| UID        | 用户名，登录华为官网的账号                                    |
| PASSWORD   | 密码，登录华为官网的账号密码                                 |
| EMAIL      | QQ邮件地址                                                     |
| EMAILCODE  | QQ邮件授权码                                                   |

![C_SO~T93~~~Y5 L7OJS6 PH](https://user-images.githubusercontent.com/62554593/201273620-1e57d6ea-3f11-48f0-b08b-0efd6ea9c3a2.png)

[QQ邮件授权码设置教程](https://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)。设置-> 账户->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

![056V7DNYS8VR$DK~R{MWCT7](https://user-images.githubusercontent.com/62554593/201148676-796927c2-2e98-4208-8763-ca5bbefbf902.png)

![2)OEIE9}$Z06DOF} W 8BAV](https://user-images.githubusercontent.com/62554593/201148533-27fb2038-8588-49de-97b0-dac2f86d9565.png)


### 4 给自己的仓库点star，可以手动启动脚本。脚本也会每天定时启动

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110003041.png)

