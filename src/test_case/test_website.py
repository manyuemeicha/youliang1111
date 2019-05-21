import pytest
import time
from src.page.login_website import LoginPage


# 注意用例的入参写上browser，以及初始化页面类时，也要传入browser
# @pytest.mark.skipif(3>2,reason="不测试网站订单")
def test_create_order(browser):
    '''网站下单'''
    login = LoginPage(browser)
    # 接收登录后跳转的菜单页面
    website_menu = login.login_success("18210532386", "111111")
    time.sleep(4)
    # 调用菜单页面加菜方法
    confirm_page=website_menu.submit_order()
    time.sleep(2)
    confirm_page.confirm_order_success()

    time.sleep(3)
    url = login.current_url()
    assert "orderid" in url
if __name__ == "__main__":
    pytest.main()


    # 只运行某个文件时
    # pytest.main("./111test_elm.py")
    # 选择运行特定的某个测试用例
    # pytest.main("./111test_elm.py::test_add")

'''
. 选择运行特定的某个测试用例
你可以按照某个测试用例的的模块，类或函数来选择你要运行的case，比如下面的方式就适合一开始在调试单个测试用例的时候。
pytest -v test_pytest_markers.py::TestClass::test_method
. 选择运行特定的某个类
>pytest -v test_pytest_markers.py::TestClass
. 多种组合
>pytest -v test_pytest_markers.py::TestClass test_pytest_markers.py::test_send_http
*  通过代码中调用 pytest（如果是使用main（）执行用例命令，单独存放在一个文件里，放在项目路径的根目录下，因为会执行当前目录下的所有用例；如果使用指定用例目录的方式，该文件位置不限制了，注意main（）里边的参数是一个列表[]）
'''


