from conftest import domain
from src.common.BasePage import Base_Page
from src.page.website_menu import WebsiteMenu


class LoginPage(Base_Page):
    # 打开登录页
    def open_login(self):
        self.open(domain+"fos-web/web/login.html")

    def user_input(self):
        return self.by_name("phone")

    def pwd_input(self):
        return self.by_name("password")

    def login_btn(self):
        return self.by_css(".s_57")

    def login_success(self,user,pwd):
        self.set_max_window()
        self.open_login()
        self.user_input().send_keys(user)
        self.pwd_input().send_keys(pwd)
        self.login_btn().click()
        return WebsiteMenu(self.driver)

# dr=webdriver.Chrome()
# lp=LoginPage(dr)
# lp.login_success("18210532386","111111")

