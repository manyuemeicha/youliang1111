from src.common.BasePage import Base_Page
from conftest import domain
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Add_Select_User(Base_Page):
    def open_add_user(self):
        self.set_max_window()
        time.sleep(15)
        self.open(domain+"fos-web/home/authority/user.jsp")
    #添加用户页面的处理，添加的断言打算用提示语和查询新增的记录是否存在两种
    def user_name_input(self):
        return self.by_id("username")
    def user_real_name_input(self):
        return self.by_id("realname")
    def phone_input(self):
        return self.by_id("telephone")
    def pwd_input(self):
        return self.by_id("password")
    def role_select(self,value):
        sel=self.by_id("role")
        return self.select_value(sel,value)
    def scope_select(self,value):
        sel=self.by_id("controlid")
        return self.select_value(sel,value)
    def permission_select(self,value):
        sel=self.by_id("groupid")
        return self.select_value(sel,value)
    def status_select(self,value):
        sel=self.by_id("isdel")
        return self.select_value(sel,value)
    def submit_btn(self):
        return self.by_id("createNewBtn")
    def spread_add_page(self):
        return self.by_xpath("// *[ @ id = 'addrow'] / div / div / div[1] / div / a / i")
    def alert_text(self):
        time.sleep(1)
        return self.by_css(".bootbox-body").text
    def ok_btn(self):
        return self.by_xpath("/html/body/div[5]/div/div/div[2]/button")
    def add_user_success(self,username):
        self.open_add_user()
        self.spread_add_page().click()
        self.user_name_input().send_keys(username)
        self.user_real_name_input().send_keys("测试zd")
        self.pwd_input().send_keys("111")
        self.phone_input().send_keys("18211112222")
        self.role_select("分店管理员")
        self.scope_select("北京·优粮生活（定慧寺桥店）")
        self.permission_select("分店管理员")
        self.status_select("冻结")
        self.submit_btn().click()
        self.alert_text=self.alert_text()
        self.ok_btn().click()
        return self.alert_text,self.select_username_success(username)  #返回弹出框的提示和查询结果，用例去用俩变量去接收，并做断言

    # 查询用户页面处理
    def search_username_input(self):
        return self.by_id("searchusername")
    def search_realname_input(self):
        return self.by_id("searchrealname")
    def search_role_input(self,value):
        sel=self.by_id("searchrole")
        return self.select_value(sel,value)
    def search_controlid_input(self,value):
        sel = self.by_id("searchcontrolid")
        return self.select_value(sel,value)
    def search_isdel_input(self, value):
        sel = self.by_id("searchisdel")
        return self.select_value(sel,value)
    def search_btn(self):
        return self.by_id("search")
    #搜索成功，列表字段里有搜索的数据，搜索一个条件，搜索多个条件
    #搜索前先添加记录
    def select_username_success(self,username):
        self.search_username_input().send_keys(username)
        time.sleep(2)
        self.search_btn().click()
        #这里要定位一组元素,用find_elements，如果只定位到一个也不怕，也是会返回列表，也可以迭代，
        # 如果是用find_element，只定位一个元素，那不能用for迭代
        list_username=self.driver.find_elements_by_xpath("//*[@id='tableTbody']/tr/td[1]")
        for i in list_username:   #上边如果没查出来数据，不会执行for循环，因为返回的是空列表，无法迭代
            if username==i.text:
                return True
            else:
                return False
        return "查询结果为空"

# 由于登录页面的验证码还没让开发去掉或者写一个万能的验证码，
# 所以我为了测试录入电话订单页面的代码是否正确，先让浏览器等了会，然后我手动登录后，再打开录入订单页面

dr=webdriver.Chrome()
adduser=Add_Select_User(dr)
username="cs"+str(time.time())
a=adduser.add_user_success(username)
print(a)
#http://test02.youliang100.com/fos-web/login/syslogin.jsp  登录页�