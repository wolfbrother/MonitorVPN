# MonitorVPN

## 配置文件configVPN.json
```json
"processname":"LetsPRO.exe:Shadowsocks.exe",
"checkperiodsecs":20,
"wifiname":"WNET"
```
+ processname: VPN程序的名字的列表，不同VPN程序名用:分割。
+ wifiname属性：只有在所指WiFi热点连接的情况下才会杀死VPN程序。
+ checkperiodsecs：查看周期，以秒计


## 运行
文件夹“可执行文件”/dist目录下有可执行文件monitorVPN.exe和配置文件configVPN.json，
双击可执行文件即可运行。

如果想后台执行，在目录下执行命令： start /b monitorVPN.exe
或者双击该目录下的start.bat。

+ 怎么杀掉后台进程：在任务管理器中杀掉同名程序。



