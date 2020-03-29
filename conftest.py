"""
@author: wanghongliang
@file: conftest.py
@time: 2020/3/29 15:11 
"""
import pytest
from py._xmlgen import html
from config.conf import *
from appium import webdriver

_driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = os.path.join(PICTURE_DIR, (report.nodeid.replace("::", "_")+".png").split("/")[-1])
            # print(file_name)
            # file_name = "1.png"
            # logfilename = os.path.join(Log_DIR, (report.nodeid.replace("::", "_")+".log").split("/")[-1])
            # print(logfilename)
            # logfilename = "F:/adblogcat" + "/" +"1.log"
            # logcat_file = open(logfilename, 'w')
            # logcmd = "adb logcat -v time"
            # poplog = subprocess.Popen(logcmd, stdout=logcat_file, stderr=subprocess.PIPE, shell=True)
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

def _capture_screenshot():
    """截图"""
    return _driver.get_screenshot_as_base64()
    # return driver.get_screenshot_as_file(name)


# 修改Environment
def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "DRV Link"
    config._metadata['接口地址'] = '***********'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


# 修改Summary
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: SVD测试中心")])
    prefix.extend([html.p("测试人员: blake.wang")])

"""
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    # cells.insert(2, html.th('Test_nodeid'))
    cells.pop(-1)  # 删除link列
    # cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    # cells.insert(2, html.td(report.nodeid))
    cells.pop(-1)  # 删除link列
    # cells.pop(2)

"""

'''
fixture作用范围
fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
- function 每一个函数或方法都会调用
- class  每一个类调用一次，一个类可以有多个方法
- module，每一个.py文件调用一次，该文件内又有多个function和class
- session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
'''

@pytest.fixture(scope='module')
def driver():
    global _driver
    print('------------open app------------')
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = AOS_VERSION
    desired_caps['deviceName'] = AOS_udid
    desired_caps['udid'] = AOS_udid
    # 包名/界面名
    desired_caps['appPackage'] = PackageName
    desired_caps['appActivity'] = PageName
    desired_caps['noReset'] = True  # 不清空缓存数据
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['automationName'] = "Uiautomator2"
    desired_caps['autoAcceptAlerts'] = True
    desired_caps['newCommandTimeout'] = 400
    desired_caps['recreateChromeDriverSessions'] = True
    _driver = webdriver.Remote('http://localhost:'+Appium_Port+'/wd/hub', desired_caps)
    yield _driver
    print('------------close app------------')
    _driver.quit()