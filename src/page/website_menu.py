from conftest import domain
from src.common.BasePage import Base_Page
from src.page.website_confirm_order import WebsiteConfirmOrder
import time


class WebsiteMenu(Base_Page):
    # 打开网站首页
    def open_website(self):
        self.set_max_window()
        self.open(domain+"fos-web/web/index.html")

    def set_address(self):
        self.by_css(".ctl_6").click()
        self.address = self.by_css("#suggestId")
        self.address.clear()
        self.address.send_keys("怀柔汽车站")
        self.by_css("#roomId").clear()
        self.by_css("#roomId").send_keys("1234")
        self.by_css(".submit").click()

    # 点击开始点餐
    def menu(self):
        self.click(self.by_link("开始订餐"))

    def add_dishes(self):

        self.by_xpath("//*[@id='8ab3344555a914520155b97c38c427fc']/div[2]/p/img").click()
        self.by_xpath("//*[@id='8ab3344555a914520155b97c38c427fc']/div[2]/p/img").click()
        self.by_xpath("//*[@id='8ab334455a94d02c015aa8d6f7267c78']/div[2]/p/img").click()

    def submit_order_btn(self):
        self.click(self.by_id("ensureBtn"))

    def submit_order(self):
        # self.open_website()
        # self.menu()
        self.set_address()
        time.sleep(4)
        self.add_dishes()
        self.submit_order_btn()
        return WebsiteConfirmOrder(self.driver)
# 调试本模块的功能  注意将submit_order方法里的前两行注释打开，且把set_address方法里的第一行注释掉
# from selenium import webdriver
# dr=webdriver.Chrome()
# wb=WebsiteMenu(dr)
# wb.submit_order()

