from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.freeconferencecall.com/global/pl')

login_button = driver.find_element('xpath', '//a[@id="login-desktop"]')
login_button.click()

email_field = driver.find_element('xpath', '//input[@id="login_email"]')
email_field.send_keys('test@test.com')
email_field_value = email_field.get_attribute('value')

assert 'test@test.com' in email_field_value

# email_field.clear()
# email_field.send_keys('fffffff')

# print(email_field.get_attribute('value'))
