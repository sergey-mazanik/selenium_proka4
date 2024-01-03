from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get('http://the-internet.herokuapp.com/dynamic_controls')

ENABLE_BUTTON = ('xpath', '//button[text()="Enable"]')
TEXT_FIELD = ('xpath', '//input[@type="text"]')

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
sleep(2)
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).click()
sleep(2)
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, 'Hello'))
sleep(2)

print('OK')

