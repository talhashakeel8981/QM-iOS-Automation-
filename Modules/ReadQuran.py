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

    def open_juz_by_index(self, juz_index):
        """
        Tap a Juz button by index safely (0 = Juz 1)
        """
        wait = WebDriverWait(self.driver, 15)
        juz_buttons_locator = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/**/XCUIElementTypeButton')

        # get all buttons currently visible
        elements = wait.until(EC.presence_of_all_elements_located(juz_buttons_locator))

        # if desired index is not found, just tap the last visible button
        if juz_index < len(elements):
            elements[juz_index].click()
        elif elements:
            elements[-1].click()  # tap last visible button
        else:
            raise Exception("No Juz buttons found")

    # def GoToBtn(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     go_to_button = (AppiumBy.ACCESSIBILITY_ID, "Go to")
    #     btn = wait.until(EC.element_to_be_clickable(go_to_button))
    #     btn.click()

    def GoToBtn(self, aya):
        """Tap Go To button, then type Aya number"""
        wait = WebDriverWait(self.driver, 10)

        # 1. Tap Go To button
        go_to_button = (AppiumBy.ACCESSIBILITY_ID, "Go to")  # button id
        go_to_btn = wait.until(EC.element_to_be_clickable(go_to_button))
        go_to_btn.click()

        # 2. Tap Aya input field and type number using correct locator
        aya_field = (AppiumBy.IOS_PREDICATE, 'value == "Aya"')
        field = wait.until(EC.element_to_be_clickable(aya_field))
        field.click()  # focus the field
        field.clear()
        field.send_keys(str(aya))

    def GoToSurahAndAya(self, surah, aya):
        """Click Go To, fill Surah name and then Aya number"""
        wait = WebDriverWait(self.driver, 10)

        # click Go To button
        go_to_button = (AppiumBy.ACCESSIBILITY_ID, "Go to")
        go_to_btn = wait.until(EC.element_to_be_clickable(go_to_button))
        go_to_btn.click()

        # fill Surah field
        surah_field = (AppiumBy.IOS_PREDICATE, 'value == "Sura"')
        field_surah = wait.until(EC.element_to_be_clickable(surah_field))
        field_surah.click()
        field_surah.clear()
        field_surah.send_keys(surah)

        # fill Aya field
        aya_field = (AppiumBy.IOS_PREDICATE, 'value == "Aya"')
        field_aya = wait.until(EC.element_to_be_clickable(aya_field))
        field_aya.click()
        field_aya.clear()
        field_aya.send_keys(str(aya))

    def TapGoButton(self):
        """Tap Go button after typing Surah and Aya"""
        wait = WebDriverWait(self.driver, 15)

        # locator from inspector
        go_button = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Go"`][2]')

        # wait for element to be clickable / visible
        element = wait.until(lambda d: d.find_element(*go_button))

        # tap using simple click
        element.click()