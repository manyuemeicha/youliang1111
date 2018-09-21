from src.page.phone_order import Phone_Order
from src.page.login_youliang import Login_Youliang
import pytest


#注意用例的入参写上browser，以及初始化页面类时，也要传入browser
def test_phone(browser):
    '''电话下单'''
    lg=Login_Youliang(browser)
    lg.login_youliang_success()

    phone=Phone_Order(browser)
    phone.create_phone_order()

    message=phone.message().text
    assert message=="录入订单成功"
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
