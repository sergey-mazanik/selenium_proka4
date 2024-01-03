
# 1. Заполнить все текстовые поля данными (почистить поля перед заполнением).
# 2. Проверить, что данные действительно введены, используя get_attribute() и assert.


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')

full_name_input = driver.find_element('xpath', '//input[@id="userName"]')
full_name_input.clear()
full_name_input.send_keys('full name')
full_name_input_value = full_name_input.get_attribute('value')
assert 'full name' in full_name_input_value

email_input = driver.find_element('xpath', '//input[@id="userEmail"]')
email_input.clear()
email_input.send_keys('email@test.com')
email_input_value = email_input.get_attribute('value')
assert 'email@test.com' in email_input_value

current_address_input = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
current_address_input.clear()
current_address_input.send_keys('current address')
current_address_input_value = current_address_input.get_attribute('value')
assert 'current address' in current_address_input_value

permanent_address_input = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')
permanent_address_input.clear()
permanent_address_input.send_keys('permanent address')
permanent_address_input_value = permanent_address_input.get_attribute('value')
assert 'permanent address' in permanent_address_input_value
