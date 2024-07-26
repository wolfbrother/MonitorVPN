[TOC]

## 项目名称

MonitorPC

## 简介
#### 项目简要描述

企业内网出于安全考虑，会限制安装和使用shadowsocks等翻墙软件，以及向日葵、todesk等远程工具。为了避免在企业内网误用这些工具，本软件可以在连接内网期间，判断这些工具是否在运行，如果有运行会立即将这些工具的程序进程杀掉，以维护企业内网安全。

其中内网WiFi的名字（SSID）、被限制软件、检查周期均可配置。

#### 项目背景
保护企业内网安全，避免在内网环境下误用限制软件。



#### 注意事项

建议以企业要求为准，本软件的可靠性没有保障。

## 安装
+ 环境要求： Windows。
+ 安装步骤：绿色软件，无需安装。
+ 运行项目： 双击可执行文件。

## 使用方法
#### 配置文件configVPN.json
```json
"processname":"LetsPRO.exe:Shadowsocks.exe",
"checkperiodsecs":5,
"wifiname":"WNET"
```
+ processname: VPN程序的名字的列表，不同VPN程序名用:分割，上面包含2个VPN程序的名字，分别是LetsPRO.exe和Shadowsocks.exe，具体的VPN名字以本机信息为准。
+ wifiname属性：WiFi热点的名字。只有在所指WiFi热点连接的情况下才会杀死VPN程序。
+ checkperiodsecs：查看周期，以秒计。满足条件的情况下，杀死VPN程序的最大时间延迟。


#### 运行
子目录下有可执行文件monitorVPN.exe和配置文件configVPN.json，
双击monitorVPN.exe即可运行。

如果想后台执行，在目录下执行命令： start /b monitorVPN.exe

+ 怎么杀掉后台进程：在任务管理器中杀掉同名程序。
常见问题和解决方案

## 功能特点
详细描述每个主要功能
额外的功能或特性
已知限制

## 技术栈
+ 使用的编程语言: Python
+ 依赖库：subprocess/hardet/psutil/time/os/json/logging/atexit

## 联系信息
jlxufly#at#gmail.com
