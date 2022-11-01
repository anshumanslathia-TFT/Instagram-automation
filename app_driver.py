import os
import pdb

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# options = UiAutomator2Options().load_capabilities({
#     # Set URL of the application under test
#     "app": "/home/anshuman-slathia/PycharmProjects/Instagram-automation/com.flipkart.android.1150200.apk",
#     # Specify device and os_version for testing
#     "platformVersion": "9.0",
#     "deviceName": "Google Pixel 3",
# })

desired_cap = {
    # Set URL of the application under test
    "app": os.getcwd() + "/com.facebook.katana_0_apps.evozi.com.apk",
    "platformVersion": "12.0",
    "platformName": "Android",
    "deviceName": "Pixel 4a",
    "appPackage": "",
    "appWaitActivity": ""
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# If you have uploaded your app, update the test case here.
# search_element = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
# )
# search_element.click()
# search_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable(
#         (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
# )
# search_input.send_keys("BrowserStack")
# time.sleep(5)
# search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
# assert (len(search_results) > 0)
# # Invoke driver.quit() after the test is done to indicate that the test is completed.
# driver.quit()
