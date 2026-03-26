import pytest
from Modules.ReadQuran import ReadQuran
from utils.driver_setup import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestReadQuran:

    @classmethod
    def setup_class(cls):
        cls.driver = create_driver()  # create iOS driver

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_open_read_quran(self):
        read_quran = ReadQuran(self.driver)
        read_quran.read_quran_module()  # tap Read Quran button
        read_quran.juzList()
