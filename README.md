# 华为状态码自动查询工具

![Stars](https://img.shields.io/github/stars/quzard/SEU_Auto_Leave.svg)
![Forks](https://img.shields.io/github/forks/quzard/SEU_Auto_Leave.svg)

## 使用步骤

1. 首先 fork 本项目到自己的仓库

2. 去 Actions 那 Enable Workflow

3. 进入自己 fork 的仓库，点击 Settings -> Secrets -> New repository secret，它们将作为配置项，在应用启动时传入程序。

**所有的可用 Secrets 及说明**

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| UID        | 用户名                                                       |
| PASSWORD   | 密码                                                         |
| EMAIL      | 邮件地址                                                     |
| EMAILCODE  | 邮件授权码                                                   |

4. 给自己的仓库点star，启动脚本
