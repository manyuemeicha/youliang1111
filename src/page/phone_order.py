from conftest import domain
from src.common.BasePage import Base_Page
from selenium.webdriver.support.select import Select

import time
class Phone_Order(Base_Page):
    def open_phone_order(self):
        return  self.open(domain+"fos-web/home/order/phoneorder.jsp")
    def city(self):
        sele=self.by_id("city")
        Select(sele).select_by_value("北京")
    def phone(self):
        return self.by_id("phone")
    def name(self):
        return self.by_id("name")
    def address(self):
        return  self.by_id("suggestId")
    def room(self):
        return self.by_id("room")
    def select_branch_btn(self):
        return self.by_id("searchBranchProductMenu")
    def mark(self):
        return self.by_id("others")
    def submit_order(self):
        return self.by_id("submit")
    def add_dishes(self):
        return self.by_xpath('//*[@id="8ab334455a94d02c015aa8d6f7267c78"]/td[5]/div/span[2]').click()
        return self.by_xpath('//*[@id="ff80808160c3ebba0160c475c52b062a"]/td[5]/div/span[2]').click()
    def message(self):
        return self.by_css(".bootbox-body")
    def create_phone_order(self):
        self.set_max_window()
        self.open_phone_order()
        self.city()
        self.phone().send_keys("18210532386")
        # self.phone().send_keys("18111132381")
        # self.name().send_keys("张先生")
        # self.address().send_keys("北京市怀柔区怀柔汽车站")
        # self.room().send_keys("1234")
        self.select_branch_btn().click()
        self.add_dishes()
        self.mark().send_keys("其他要求1，其他要求2")
        self.submit_order().click()

#由于登录页面的验证码还没让开发去掉或者写一个万能的验证码，
# 所以我为了测试录入电话订单页面的代码是否正确，先让浏览器等了会，然后我手动登录后，再打开录入订单页面
# from selenium import webdriver
# dr=webdriver.Chrome()
# p=Phone_Order(dr)
# time.sleep(20)
# p.create_phone_order()


