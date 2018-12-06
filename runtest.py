import pytest
import time
from src.common import send_mail

# now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
# fp="./report/"+now_time+"report.html"

fp = "./report/report.html"
pytest.main(["-s","./src/test_case/","--html="+fp,"--self-contained-html"])
# pytest命令行执行默认不会打印log信息，需要加‘-s’参数或者 ‘–capture=no’，即pytest -s
# 生成html需要安装pytest-html模块  pip show pytest-html
# --html=**生成的报告，css是独立的，分享报告的时候样式会丢失，为了更好的分享发邮件展示报告，
# 可以把css样式合并到html里，即在pytest.main()里加上--self-contained-html参数


# send_mail.send_mail(fp)





'''
首次失败后停止执行,即有一个用例失败就停止执行：py.test -x  x代表exit
# pytest.main(["-s","-x","./src/test_case/","--html=./report/"+now_time+"report.html"])
两次失败之后停止执行，即有2个用例失败后就停止执行：py.test --maxfail = 2
# pytest.main(["-s","--maxfail=1","./src/test_case/","--html=./report/"+now_time+"report.html"])
'''


