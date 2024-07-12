# MonitorVPN

## 配置文件configVPN.json
```json
"processname":"LetsPRO.exe:Shadowsocks.exe",
"checkperiodsecs":20,
"wifiname":"WNET"
```
+ processname: VPN程序的名字的列表，不同VPN程序名用:分割，上面包含2个VPN程序的名字，分别是LetsPRO.exe和Shadowsocks.exe，具体的VPN名字以本机信息为准。
+ wifiname属性：WiFi热点的名字。只有在所指WiFi热点连接的情况下才会杀死VPN程序。
+ checkperiodsecs：查看周期，以秒计。满足条件的情况下，杀死VPN程序的最大时间延迟。


## 运行
子目录下有可执行文件monitorVPN.exe和配置文件configVPN.json，
双击monitorVPN.exe即可运行。

如果想后台执行，在目录下执行命令： start /b monitorVPN.exe

+ 怎么杀掉后台进程：在任务管理器中杀掉同名程序。



