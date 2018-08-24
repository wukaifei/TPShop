from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MinePage(BaseAction):
    sign_up_button = By.XPATH, "//*[@text='登录/注册']"

    def click_sign_up(self):
        self.click(self.sign_up_button)
