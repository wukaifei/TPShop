import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10.0, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(location_by, location_value))
        # return self.driver.find_element(location_by, location_value)

    def find_elements(self, location, timeout=10.0, poll=1.0):
        location_by, location_value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(location_by, location_value))

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = self.find_element((By.XPATH, message), timeout=timeout, poll=0.1)
        return element.text

    def is_toast_exist(self, message):
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False