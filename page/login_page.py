import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    input_phone_text = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_phone_num']"
    input_password_text = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_password']"
    login_button = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/btn_login']"

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

    def is_login_button_enabled(self):
        return self.is_login_button_enabled(self.login_button)