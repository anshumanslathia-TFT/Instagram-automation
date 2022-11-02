import os
import pdb
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


desired_cap = {
    # Set URL of the application under test
    "app": os.getcwd() + "/com.flipkart.android.1150200.apk",
    "platformVersion": "13",
    "platformName": "Android",
    "deviceName": "Pixel 6 Pro",
    "appPackage": "",
    "appWaitActivity": "",
    'newCommandTimeout': 20000,
    'deviceReadyTimeout': 2000
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
# import pdb; pdb.set_trace()
# If you have uploaded your app, update the test case here.
select_language = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='English']")))

select_language.click()
continue_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (AppiumBy.XPATH, "//android.widget.Button[@text='CONTINUE']"))
)
time.sleep(5)
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert (len(search_results) > 0)
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
