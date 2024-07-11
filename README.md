# MonitorVPN

## 配置文件configVPN.json
'''json
"processname":"LetsPRO.exe:Shadowsocks.exe",
"checkperiodsecs":20,
"wifiname":"WNET"
'''
+ processname: VPN程序的名字的列表，不同VPN程序名用:分割。
+ wifiname属性：只有在所指WiFi热点连接的情况下才会杀死VPN程序。
+ checkperiodsecs：查看周期，以秒计

