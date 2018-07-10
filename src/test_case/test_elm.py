from src.page.elm_order import Elm_Order
import pytest
from db_fixture.mysql_db import DB
#@pytest.mark.skipif(3>2,reason="测试")
def test_elm():
    db=DB()
    db.clear("order_push_record","饿了么")


    r=Elm_Order()
    assert "ok" in r.elm_order()
    db.update("饿了么")
    db.close()
if __name__=='__main__':
        pytest.main("./test_elm.py")
        #只运行某个文件时
        #pytest.main("./test_elm.py")
        #选择运行特定的某个测试用例
        #pytest.main("./test_elm.py::test_add")

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