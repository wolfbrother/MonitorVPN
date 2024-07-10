# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:21:04 2024

@author: jlxuf
"""
import subprocess
import chardet
import psutil
import time
import os
import json
import logging

log_directory = os.path.dirname(os.path.abspath(__file__))
log_filename = 'killVPNlog.log'
log_file_path = os.path.join(log_directory, log_filename)
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
    handlers=[
        logging.FileHandler(log_file_path),  # 将日志写入文件
        #logging.StreamHandler()  # 同时在控制台输出日志
    ]
)

 
def get_connected_wifi_name():
    process = subprocess.Popen(['netsh', 'wlan', 'show', 'interfaces'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    detected_encoding = chardet.detect(stdout)['encoding']
    
    for line in stdout.decode(detected_encoding).splitlines():
        if 'SSID' in line:
            ssid = line.split(':')[1].strip()
            return ssid
 
    return None

def kill_process_by_name(process_name = "LetsPRO.exe"):
    # # tasklist | findstr "Lets"
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 检查进程名称是否匹配
            if proc.info['name'] == process_name:
                logger.info(f"Killing process {process_name} with PID {proc.info['pid']}")
                #print(f"Killing process {process_name} with PID {proc.info['pid']}")
                proc.terminate()  # 尝试优雅地终止进程
                proc.wait(timeout=3)  # 等待进程终止
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def isNamedWifiConnected(wifi = "WNET"):
    
 
    wifi_name = get_connected_wifi_name()
    return wifi_name == wifi

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def getProcessName():
    current_directory = os.getcwd()

    json_filename = 'configVPN.json'

    json_file_path = os.path.join(current_directory, json_filename)
    
    encoding = detect_encoding(json_file_path)

    with open(json_file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    
    processname = data.get('processname')
    
    return processname

# 配置日志




logger = logging.getLogger(__name__)
logger.info("started")
    
process_name = getProcessName()#"LetsPRO.exe"
while True:
    logger.info("check again")
    time.sleep(60)
    isConnected = isNamedWifiConnected()
    if isConnected:
        kill_process_by_name(process_name)
    
