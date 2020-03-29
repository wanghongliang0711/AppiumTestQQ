"""
@author: wanghongliang
@file: conf.py
@time: 2020/3/29 15:12 
"""
import os
import datetime

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# 当前时间
CURRENT_TIME = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")

# 报告名称
HTML_NAME = f"testReport{CURRENT_TIME}.html"

# AOS系统版本
AOS_VERSION = "8"
# APP版本
# APP_VERSION = "V 0.0.7.1"
# APP_VERSION = "V 0.0.8.1"
# 系统语言
# system_language = "English"
# 手机型号
phone_model = "VIVO"
# 端口
Appium_Port = "4723"
# adb devices 命令获取
# AOS_udid = "R28M619B6PZ"
AOS_udid = "6TV44HNV5HAYVWZ9"
#S10 R28M619B6PZ
# 442ad8ef
# vivo 6TV44HNV5HAYVWZ9
# 测试软件包名
PackageName = "com.tencent.mobileqq"
# 测试软件界面名
PageName = ".activity.SplashActivity"