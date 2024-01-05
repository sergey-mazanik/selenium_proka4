from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://demoqa.com/alerts')

BUTTON_1 = ('xpath', '//button[@id="alertButton"]')
BUTTON_3 = ('xpath', '//button[@id="confirmButton"]')
BUTTON_4 = ('xpath', '//button[@id="promtButton"]')
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert
print(alert.text)
alert.send_keys('Hello')
alert.accept()
