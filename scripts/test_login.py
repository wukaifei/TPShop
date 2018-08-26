import pytest
import time
import random
from selenium.webdriver.common.by import By

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def show_password_data():
    temp_list = list()
    for i in range(2):
        temp_list.append(random_password())

class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login(self,args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     self.page.first.click_mine()
    #     self.page.mine.click_sign_up()
    #     self.page.login.input_phone(username)
    #     self.page.login.input_pwd(password)
    #     self.page.login.click_login()
    #     assert self.page.login.is_toast_exist(expect)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_miss_part"))
    # def test_login_miss_part(self,args):
    #     username = args["username"]
    #     password = args["password"]
    #
    #     self.page.first.click_mine()
    #     time.sleep(2)
    #     self.page.mine.click_sign_up()
    #     self.page.login.input_phone(username)
    #     self.page.login.input_pwd(password)
    #     assert not self.page.login.is_login_button_enabled()

    @pytest.mark.parametrize("password", show_password_data())
    def test_show_password(self, password):
        password_location = (By.XPATH, "//*[@text='%s']" % password)

        self.page.first.click_mine()
        self.page.mine.click_sign_up()
        self.page.login.input_pwd(password)
        # 在点击眼睛之前，没有找到输入的密码
        assert not self.page.login.find_element(password_location)
        self.page.login.click_view_pwd()
        assert self.page.login.is_location_exist(password_location)
