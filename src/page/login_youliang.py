from conftest import domain
from src.common.BasePage import Base_Page
class Login_Youliang(Base_Page):
    def open_youliang(self):
        return self.open(domain+"fos-web/login/syslogin.jsp")
    def user_input(self):
        return self.by_id("loginUsername")
    def pwd_input(self):
        return self.by_id("loginPassword")
    def login_btn(self):
        return self.by_id("loginButton")
    def login_youliang_success(self):
        self.open_youliang()
        self.user_input().send_keys("super")
        self.pwd_input().send_keys("111")  #这里要参数化  方法入参
        self.login_btn().click()

