from src.common.BasePage import Base_Page
import time


class WebsiteConfirmOrder(Base_Page):
    def candaofukuan_btn(self):
        return self.by_id("offlinePay")

    def confirm_order_btn(self):
        return self.by_id("submit")

    def confirm_order_success(self):
        self.candaofukuan_btn().click()
        self.confirm_order_btn().click()
        time.sleep(2)
