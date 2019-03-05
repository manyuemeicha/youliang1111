import pytest
from selenium import webdriver
import os
from datetime import datetime
from py.xml import html


domain = "http://test02.youliang100.com/"
elm_url = "http://test02.youliang100.com/elemv2/push"
baidu_url = "http://test02.youliang100.com/thirdparty/baidu/baiduorderdo"
meituan_url = "http://test02.youliang100.com/thirdparty/meituan/receivemeituanorder"

driver = None  # 定义一个全局变量，方便自动截图函数里调用get_screenshot_as_file(),前提是先在browser()里给driver赋值


# 整个测试只启动一次一浏览器，所有模块共用一个浏览器驱动
@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver


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
            screen_name = "./report/image/"+report.nodeid.replace("::", "_").replace("src/test_case/","")+".png"
            # （！重要！）对参数化了的用例，参数包含中文，即report.nodeid包含中文的用例获取的图片名称，例如./report/image/test_02.py_test_02[/u54c8].png
            # 节点后边跟着的参数包含中文，但是显示有问题，所以需要按照将报告里的nodeid包含中文需要转码的方法，对该screen_name进行转码，否则截图会失败，只有
            #只有转为文字，截图才会成功
            screen_name = screen_name.encode("utf-8").decode("unicode_escape")  
            _capture_screenshot(screen_name)
            # 这里再定义一个图片路径的原因是报告里的显示的图片的路径是相当于当前报告文件的，如果还用screen_name，
            # 那报告里肯定找不到图片的，因为路径显示不对，所以重新定义一个相对于当前报告文件的图片路径，让报告文件能显示图片
            image_path=screen_name.replace("./report/image/","./image/")
            if screen_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % image_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        
        
        report.description = str(item.function.__doc__) # 给报告里的【Descript】列赋值
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 给报告里的【Test_nodeid】列赋值，
                                                                        # 目的是将节点里的参数包含中文部分进行转码，例如，
                                                                         # 将src/test_case/test_01.py::test_001[/u54c8].
                                                                        # 转码为src/test_case/test_01.py::test_001[绿萝]，使中文正常显示


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


#以下俩函数和pytest_runtest_makereport()钩子函数的最后两句；是为了在报告里添加Description列（用例描述/注释）,Time列（获取当前时间），
# 去掉原有的Test列，因为里边的中文显示有编码问题，重新添加Test_nodeid列，并将节点的参数化部分包含中文的进行转码，
# 保证中文显示正常
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))  # 添加Description列
    cells.insert(1, html.th('Test_nodeid'))  # 添加Test_nodeid列,
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))  # 添加Time列
    cells.pop(3)  # 删除Test列

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))  # 用pytest_runtest_makereport()钩子函数里的report.description变量给每行复制
    cells.insert(1, html.td(report.nodeid))   # 用pytest_runtest_makereport()钩子函数里的report.nodeid变量给每行复制
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))  # utcnow()是获取当前时间，用当前时间给Time列的每行赋值
    cells.pop(3)  # 删除Test列的行内容
    

# 当用pytets做接口自动化时（注意是接口自动化，因为做web自动化，关注页面，失败会自动截图）
# 加上下边的内容 3个函数，将接口的返回显示在报告上（也可以显示非json形式的返回结果，只要是请求的返回都可以显示，
# 那么接收用例请求的返回值就要用r.text（返回的是字符串类型，unicode字符；会自动根据响应头部的字符编码进行解码）
# 或者r.content（字节形式，byte对象，适用于压缩后的或者图片/文件），但是一般是测试页面html的返回才会是非json，看测试页面的返回结果没什么意义，
# 所以用r.text比较好），
# 以及添加可排序的Time时间列，和删除Links列
# 注意！！！必须将这三个函数放在添加描述列的后边，否则不生效
# 注意！！！！每一条用例方法里加一个return 返回接口的返回结果，用于显示在html上
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Response'))     # 添加列名
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))  # 这句虽然在上边的添加描述列的相关函数里写了，
                                                                          # 但是这里也要写，否则time列不显示
    cells.pop()         # 这句虽然在上边的添加描述列函数里写了，但是这里也要写，否则links还显示
                        # 也可以将这两句从上边的添加描述列的相关函数里删除，貌似只能在最后执行的代码里写上才会执行


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.response))   # 给response每一行赋值
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))  # 这句虽然在上边的添加描述列的相关函数里写了，
                                                                        # 但是这里也要写，否则time列不显示
    cells.pop()  # 这句虽然在上边的添加描述列函数里写了，但是这里也要写，否则links还显示
                 # 也可以将这两句从上边的添加描述列的相关函数里删除，貌似只能在最后执行的代码里写上才会执行


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.response = str(item.function())   # 每一条用例里加一个return 返回接口的返回结果
                                         # 这里调用函数，来获取函数返回值，即接口的返回结果，
                                         # 显示在html的【Response】列





# @pytest.fixture(scope="function", autouse=True)
# def ft():
#     print("fixture-test!!!")


'''
    driver = Remote(command_executor='http://192.168.44.129:5557/wd/hub',
                    desired_capabilities={
                          "browserName": "firefox",
                    })
'''



