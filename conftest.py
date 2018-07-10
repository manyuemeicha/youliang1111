import pytest
from selenium import webdriver
import os

domain="http://test02.youliang100.com/"
elm_url="http://test02.youliang100.com/elemev2/push"
baidu_url="http://test02.youliang100.com/thirdparty/baidu/baiduorderdo"
meituan_url="http://test02.youliang100.com/thirdparty/meituan/receivemeituanorder"

driver = None  #定义一个全局变量，方便自动截图函数里调用get_screenshot_as_file(),前提是先在browser()里给driver赋值

#整个测试只启动一次一浏览器，所有模块共用一个浏览器驱动
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

# @pytest.fixture(scope="function", autouse=True)
# def ft():
#     print("fixture-test!!!")


'''
    driver = Remote(command_executor='http://192.168.44.129:5557/wd/hub',
                    desired_capabilities={
                          "browserName": "firefox",
                    })
'''

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)