from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import os
import cv2
import numpy as np


class ReadQuran:
    def __init__(self, driver):
        self.driver = driver

        # Improved locators (more stable for iOS)
        self.read_quran_button = (
            AppiumBy.IOS_PREDICATE,
            'label == "Read Quran"'
        )

        self.juz_selector_button = (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeButton[2]'
        )

    # ---------- COMMON SAFE ACTION ----------
    def safe_click(self, locator, retries=3):
        wait = WebDriverWait(self.driver, 15)

        for _ in range(retries):
            try:
                element = wait.until(EC.presence_of_element_located(locator))
                element.click()
                return
            except StaleElementReferenceException:
                time.sleep(1)

        raise Exception(f"Element not stable: {locator}")

    # ---------- NAVIGATION ----------
    def read_quran_module(self):
        wait = WebDriverWait(self.driver, 15)

        # Ensure screen is loaded
        wait.until(EC.presence_of_element_located(self.read_quran_button))

        self.safe_click(self.read_quran_button)
        time.sleep(2)   # allow screen transition

    def juzList(self):
        self.safe_click(self.juz_selector_button)
        time.sleep(2)

    def open_juz_by_index(self, juz_index):
        wait = WebDriverWait(self.driver, 15)

        locator = (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeScrollView/**/XCUIElementTypeButton'
        )

        elements = wait.until(EC.presence_of_all_elements_located(locator))

        if not elements:
            raise Exception("No Juz buttons found")

        index = min(juz_index, len(elements) - 1)
        elements[index].click()

        time.sleep(2)

    # ---------- GO TO ----------
    def GoToSurahAndAya(self, surah, aya):
        wait = WebDriverWait(self.driver, 15)

        go_to_button = (AppiumBy.ACCESSIBILITY_ID, "Go to")
        self.safe_click(go_to_button)

        # Surah
        surah_field = (AppiumBy.IOS_PREDICATE, 'value == "Sura"')
        field_surah = wait.until(EC.presence_of_element_located(surah_field))
        field_surah.click()
        field_surah.clear()
        field_surah.send_keys(surah)

        # Aya
        aya_field = (AppiumBy.IOS_PREDICATE, 'value == "Aya"')
        field_aya = wait.until(EC.presence_of_element_located(aya_field))
        field_aya.click()
        field_aya.clear()
        field_aya.send_keys(str(aya))

    def TapGoButton(self):
        go_button = (
            AppiumBy.IOS_CLASS_CHAIN,
            '**/XCUIElementTypeButton[`name == "Go"`][2]'
        )
        self.safe_click(go_button)
        time.sleep(3)   # wait for page load

    # ---------- IMAGE VERIFICATION ----------
    def VerifyPageByImage(self, reference_filename="anaam.png", crop_top=200, crop_bottom=110):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        reference_path = os.path.normpath(
            os.path.join(base_dir, "..", "image", reference_filename)
        )

        if not os.path.exists(reference_path):
            raise FileNotFoundError(f"Reference image not found: {reference_path}")

        screenshot_bytes = self.driver.get_screenshot_as_png()
        actual_array = np.frombuffer(screenshot_bytes, dtype=np.uint8)
        actual_img = cv2.imdecode(actual_array, cv2.IMREAD_COLOR)

        reference_img = cv2.imread(reference_path)

        if actual_img.shape != reference_img.shape:
            actual_img = cv2.resize(
                actual_img,
                (reference_img.shape[1], reference_img.shape[0])
            )

        # Crop top and bottom margins
        actual_cropped = actual_img[crop_top:-crop_bottom, :]
        reference_cropped = reference_img[crop_top:-crop_bottom, :]

        diff = cv2.absdiff(actual_cropped, reference_cropped)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

        diff_pixels = cv2.countNonZero(thresh)
        total_pixels = gray.shape[0] * gray.shape[1]

        similarity = ((total_pixels - diff_pixels) / total_pixels) * 100

        print(f"\nDiff pixels: {diff_pixels}")
        print(f"Similarity : {similarity:.2f}%")

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        result_img = actual_cropped.copy()

        for c in contours:
            if cv2.contourArea(c) > 50:
                x, y, w, h = cv2.boundingRect(c)
                cx, cy = x + w // 2, y + h // 2
                radius = max(w, h) // 2 + 10
                cv2.circle(result_img, (cx, cy), radius, (0, 0, 255), 3)

        diff_output = os.path.normpath(
            os.path.join(base_dir, "..", "image", "diff_" + reference_filename)
        )
        cv2.imwrite(diff_output, result_img)

        assert diff_pixels == 0, (
            f"Mismatch detected: {diff_pixels} pixels different "
            f"({similarity:.2f}% similar). See {diff_output}"
        )
