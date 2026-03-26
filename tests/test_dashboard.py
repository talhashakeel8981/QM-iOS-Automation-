import unittest
from utils.driver_setup import create_driver

class TestReadQuran(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_open_read_quran(self):
        # wait for the element
        self.driver.implicitly_wait(10)

        # tap the Read Quran button
        read_quran_btn = self.driver.find_element("accessibility id", "Read Quran")
        read_quran_btn.click()

        print("Tapped Read Quran successfully")

if __name__ == "__main__":
    unittest.main()