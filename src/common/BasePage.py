from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Base_Page():
    def __init__(self,driver):
        self.driver=driver
    def current_url(self):
        return self.driver.current_url
    def open(self,url):
        return self.driver.get(url)
    def element_wait(self,sec,type,value):
        '''显示等待'''
        return WebDriverWait(self.driver,sec,0.5).until(EC.presence_of_element_located(By.type,value))
    def by_id(self,value):
        return self.driver.find_element_by_id(value)
    def by_name(self,value):
        return self.driver.find_element_by_name(value)
    def by_link(self,value):
        return self.driver.find_element_by_link_text(value)

    def by_partial_link(self,value):
        return self.driver.find_element_by_partital_link_text(value)

    def by_css(self,value):
        return self.driver.find_element_by_css_selector(value)
    def by_class_name(self,value):
        return self.driver.find_element_by_class_name(value)
    def by_xpath(self,value):
        return self.driver.find_element_by_xpath(value)
    def select_value(self,sel,value):
        return Select(sel).select_by_visible_text(value)
    def click(self,element):
        return element.click()
    def set_max_window(self):
        return self.driver.maximize_window()
    # def accept_alert(self):
    #     return self.driver.switch_to_alert().accpet()
    # def get_alert_text(self):
    #     return self.driver.switch_to_alert().text

