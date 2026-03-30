import base64
import io
import os
from PIL import Image, ImageChops

from Modules.ReadQuran import ReadQuran
from utils.driver_setup import create_driver

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

    def test_open_specific_juz(self):
        read_quran = ReadQuran(self.driver)
        read_quran.read_quran_module()
        read_quran.juzList()
        read_quran.open_juz_by_index(juz_index=4)  # taps Juz 3 if visible

    # def test_goTo(self):
    #     read_quran = ReadQuran(self.driver)
    #     read_quran.read_quran_module()
    #     read_quran.juzList()
    #     read_quran.GoToBtn()

    def test_goTo(self):
        read_quran = ReadQuran(self.driver)
        read_quran.read_quran_module()
        read_quran.juzList()

        # type surah and aya
        read_quran.GoToSurahAndAya("Al-Fatiha", 5)

        # tap Go button
        read_quran.TapGoButton()
    # def test_goTo(self):
    #     read_quran = ReadQuran(self.driver)
    #     read_quran.read_quran_module()
    #     read_quran.juzList()
    #     read_quran.GoToSurahAndAya("Al-Anfal", 1)
    #     read_quran.TapGoButton()
    #     read_quran.VerifyPageByImage("anfalp1.png")  # page verification add