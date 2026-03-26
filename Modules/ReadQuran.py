from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReadQuran:
    def __init__(self, driver):
        self.driver = driver
        self.read_quran_button = (AppiumBy.ACCESSIBILITY_ID, "Read Quran")
        self.juz_selector_button = (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeButton[2]'
        )
    def read_quran_module(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.read_quran_button))
        button.click()

    def juzList(self):
        wait = WebDriverWait(self.driver, 10)
        juz_button = wait.until(EC.element_to_be_clickable(self.juz_selector_button))
        juz_button.click()