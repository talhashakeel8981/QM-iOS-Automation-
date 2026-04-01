import time
import pytest

from Modules.ReadQuran import ReadQuran
from utils.driver_setup import create_driver


class TestReadQuran:

    @classmethod
    def setup_class(cls):
        cls.driver = create_driver()
        cls.bundle_id = "com.pakdata.QuranMajeedLite"
        time.sleep(3)  # wait for app to fully load

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self):
        # make sure app is active, do NOT terminate
        try:
            self.driver.activate_app(self.bundle_id)
        except Exception:
            # if app not running, start via driver
            pass
        time.sleep(1)
    def test_open_read_quran(self):
        read_quran = ReadQuran(self.driver)

        read_quran.read_quran_module()
        read_quran.juzList()

    def test_open_specific_juz(self):
        read_quran = ReadQuran(self.driver)

        read_quran.read_quran_module()
        read_quran.juzList()
        read_quran.open_juz_by_index(4)

    def test_goTo(self):
        read_quran = ReadQuran(self.driver)

        read_quran.read_quran_module()
        read_quran.juzList()
        read_quran.GoToSurahAndAya("Al-Fatiha", 5)
        read_quran.TapGoButton()

    def Goto_by_Surah_Name_With_AyahNumber(self):
        read_quran = ReadQuran(self.driver)

        read_quran.read_quran_module()
        read_quran.juzList()
        read_quran.GoToSurahAndAya("anaam", 1)
        read_quran.TapGoButton()
        time.sleep(5)
        read_quran.VerifyPageByImage("anaam.png")
        time.sleep(5)

    def Goto_by_page_number(self):
        read_quran = ReadQuran(self.driver)

        read_quran.read_quran_module()
        read_quran.juzList()

        # new input type (page instead of surah/ayah)
        read_quran.GoToPage(98)

        read_quran.TapGoButton()
        time.sleep(5)

        read_quran.VerifyPageByImage("98.png")
        time.sleep(5)