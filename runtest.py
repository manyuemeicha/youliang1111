import pytest
import time
from src.common import send_mail

# now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
# fp="./report/"+now_time+"report.html"

fp="./report/report.html"
pytest.main(["-s","./src/test_case/","--html="+fp,"--self-contained-html"])
#pytest命令行执行默认不会打印log信息，需要加‘-s’参数或者 ‘–capture=no’，即pytest -s
#--self-contained-html  不加这个参数的话 发送邮件的报告附件里没有样式
#send_mail.send_mail(fp)





'''
首次失败后停止执行,即有一个用例失败就停止执行：py.test -x  x代表exit
# pytest.main(["-s","-x","./src/test_case/","--html=./report/"+now_time+"report.html"])
两次失败之后停止执行，即有2个用例失败后就停止执行：py.test --maxfail = 2
# pytest.main(["-s","--maxfail=1","./src/test_case/","--html=./report/"+now_time+"report.html"])
'''


