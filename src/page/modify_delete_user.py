from src.common.BasePage import Base_Page
from conftest import domain
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Modify_Delete_User(Base_Page):
    def open_modify_user_page(self):
        self.set_max_window()
        time.sleep(15)
        self.open(domain + "fos-web/home/authority/user.jsp")
        self.by_id("")

    def user_name_input(self):
        return self.by_id("username")

    def user_real_name_input(self):
        return self.by_id("realname")

    def phone_input(self):
        return self.by_id("telephone")

    def pwd_input(self):
        return self.by_id("password")

    def role_select(self, value):
        sel = self.by_id("role")
        return self.select_value(sel, value)

    def scope_select(self, value):
        sel = self.by_id("controlid")
        return self.select_value(sel, value)

    def permission_select(self, value):
        sel = self.by_id("groupid")
        return self.select_value(sel, value)

    def status_select(self, value):
        sel = self.by_id("isdel")
        return self.select_value(sel, value)

    def submit_btn(self):
        return self.by_id("createNewBtn")

    def spread_add_page(self):
        return self.by_xpath("// *[ @ id = 'addrow'] / div / div / div[1] / div / a / i")

    def alert_text(self):
        time.sleep(1)
        return self.by_css(".bootbox-body").text

    def add_user_success(self, username):
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
        return self.alert_text()
        # 由于登录页面的验证码还没让开发去掉或者写一个万能的验证码，
        # 所以我为了测试录入电话订单页面的代码是否正确，先让浏览器等了会，然后我手动登录后，再打开录入订单页面


dr = webdriver.Chrome()
adduser = Add_User(dr)
print(adduser.add_user_success("cs1"))
# http://test02.youliang100.com/fos-web/login/syslogin.jsp  登录页面网址
# http://test02.youliang100.com/fos-web/login/syslogin.jsp  登录页面网址