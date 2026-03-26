from appium.webdriver.common.appiumby import AppiumBy

class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        # Locator for Read Quran button
        self.read_quran_button = (AppiumBy.ACCESSIBILITY_ID, "Read Quran")

    def click_read_quran(self):
        self.driver.find_element(*self.read_quran_button).click()