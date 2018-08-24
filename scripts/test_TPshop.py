from base.base_driver import init_driver
from page.page import Page


class TestTPShop:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_tpshop(self):
        self.page.first.click_mine()
        self.page.mine.click_sign_up()
        self.page.login.input_phone("13800138006")
        self.page.login.input_pwd("123456")
        self.page.login.click_login()
