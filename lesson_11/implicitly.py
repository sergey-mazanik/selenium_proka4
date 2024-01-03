from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get('https://demoqa.com/dynamic-properties')

VISIBLE_AFTER_5_SECOND_BUTTON = ("xpath", "//button[@id='visibleAfter']")
driver.find_element(*VISIBLE_AFTER_5_SECOND_BUTTON).click()
