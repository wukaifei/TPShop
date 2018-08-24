from page.first_page import FirstPage
from page.mine_page import MinePage
from page.login_page import LoginPage


class Page:

    def __init__(self, driver):
        self.driver = driver


    @property
    def first(self):
        return FirstPage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)




