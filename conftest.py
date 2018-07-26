import pytest
from selenium import webdriver
import os

domain="http://test02.youliang100.com/"
elm_url="http://test02.youliang100.com/elemv2/push"
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

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            '''
            screen_name =  + report.nodeid.replace("::", "_") + ".png"
            screen_name的结果是失败的用例的所在路径即src/test_case/用例文件::test用例，预期这里
            存失败用例命名的图片，所以把::改为_,再加上.png，但是我们希望它存到report/image路径里，
            截图的代码写在conftest.py里，所以路径要相对于该文件，即前边加上"./report/image/"，这样截图就会进report/image里
            '''
            screen_name ="./report/image/"+report.nodeid.replace("::", "_").replace("src/test_case/","")+".png"
            _capture_screenshot(screen_name)
            #这里再定义一个图片路径的原因是报告里的显示的图片的路径是相当于当前报告文件的，如果还用screen_name，
            #那报告里肯定找不到图片的，因为路径显示不对，所以重新定义一个相对于当前报告文件的图片路径，让报告文件能显示图片
            image_path=screen_name.replace("./report/image/","./image/")
            if screen_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % image_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

