from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    input_phone_text = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_phone_num']"
    input_password_text = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/edit_password']"
    click_login_button = By.XPATH, "//*[@resource-id='com.tpshop.malls:id/btn_login']"


    def input_phone(self, text):
        self.input(self.input_phone_text, text)

    def input_pwd(self, text):
        self.input(self.input_password_text, text)

    def click_login(self):
        self.click(self.click_login_button)

