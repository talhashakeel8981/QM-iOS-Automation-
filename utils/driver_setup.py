from appium import webdriver
from appium.options.ios import XCUITestOptions

def create_driver():
    opts = XCUITestOptions()
    opts.platform_name = "iOS"
    opts.platform_version = "18.3"          # match installed runtime
    opts.device_name = "iPhone 16 Pro"
    opts.app = "/Users/muhammadtalhashakeel/QM_iOS/app/QuranMajeedLite.app"
    opts.bundle_id = "com.pakdata.QuranMajeedLite"  # add this line
    # exactly as listed by simctl
    opts.automation_name = "XCUITest"
    opts.use_new_wda = True
    opts.no_reset = True
    opts.new_command_timeout = 300

    driver = webdriver.Remote("http://127.0.0.1:4723", options=opts)
    return driver