from appium import webdriver


def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.49.101:5555'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app 信息
    desired_caps['appPackage'] = 'com.tpshop.malls'
    desired_caps['appActivity'] = '.SPMainActivity'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
