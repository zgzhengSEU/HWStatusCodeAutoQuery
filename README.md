# 华为状态码自动查询工具
华为状态码自动查询工具，全天候24h监测状态码，爱信等ALL IN！！！

![Stars](https://img.shields.io/github/stars/zgzhengSEU/HWStatusCodeAutoQuery.svg)
![Forks](https://img.shields.io/github/forks/zgzhengSEU/HWStatusCodeAutoQuery.svg)

## 使用步骤

### 1 首先点击右上角 fork 本项目到自己的仓库
  
  ![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211102351300.png)

### 2 去 Actions 那 Enable Workflow

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211102359648.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110000533.png)

### 3 进入自己 fork 的仓库，点击 Settings -> Secrets -> New repository secret，添加下列Secret供脚本使用。

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110006864.png)

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110007092.png)

必须填写下面所有的secret

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| UID        | 用户名                                                       |
| PASSWORD   | 密码                                                         |
| EMAIL      | 邮件地址                                                     |
| EMAILCODE  | 邮件授权码                                                   |

### 4给自己的仓库点star，可以手动启动脚本，脚本也会每天定时启动

![](https://cdn.jsdelivr.net/gh/zgzhengSEU/imagebed/Image/202211110003041.png)

### 参考

https://www.nowcoder.com/discuss/1093196
