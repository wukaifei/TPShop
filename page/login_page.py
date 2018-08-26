import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名
    input_phone_text = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_phone_num']"
    # 密码
    input_password_text = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_password']"
    # 登录
    login_button = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/btn_login']"
    # 显示密码
    view_pwd_button = By.XPATH, "com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_phone(self, text):
        allure.attach("用户名：", text)
        self.input(self.input_phone_text, text)

    @allure.step(title="输入密码")
    def input_pwd(self, text):
        allure.attach("密码：", text)
        self.input(self.input_password_text, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)

    @allure.step(title="点击显示密码")
    def click_view_pwd(self):
        self.click(self.view_pwd_button)

    def is_login_button_enabled(self):
        return self.is_login_button_enabled(self.login_button)
