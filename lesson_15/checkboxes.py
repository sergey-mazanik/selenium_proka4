from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# -------- Чекбокс пример 1 ----------
# CHECKBOX_1 = ('xpath', '(//input[@type="checkbox"])[1]')
# driver.get('http://the-internet.herokuapp.com/checkboxes')

# -------- Нажатие на чекбокс и проверка через получение атрибута ----------
# print(driver.find_element(*CHECKBOX_1).get_attribute('checked'))
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).get_attribute('checked'))
# # assert driver.find_element(*CHECKBOX_1).get_attribute('checked') is not None
# # assert driver.find_element(*CHECKBOX_1).get_attribute('checked') == 'true'

# -------- Нажатие на чекбокс и проверка через встроенный метод ----------
# print(driver.find_element(*CHECKBOX_1).is_selected())
# driver.find_element(*CHECKBOX_1).click()
# print(driver.find_element(*CHECKBOX_1).is_selected())


# -------- Checkbox пример 2 ----------
# CHECKBOX_HOME_STATUS = ('xpath', '//input[@id="tree-node-home"]')
# CHECKBOX_HOME_ACTION = ('xpath', '//label[@for="tree-node-home"]')
# driver.get('https://demoqa.com/checkbox')
#
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
# driver.find_element(*CHECKBOX_HOME_ACTION).click()
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())


# -------- Checkbox пример 3 ----------
# ELEMENT_ONE = ('xpath', '//li[text()="Cras justo odio"]')
# driver.get('https://demoqa.com/selectable')
#
# before = driver.find_element(*ELEMENT_ONE).get_attribute('class')
# print(before)
# driver.find_element(*ELEMENT_ONE).click()
# after = driver.find_element(*ELEMENT_ONE).get_attribute('class')
# print(after)
# assert 'active' in after


# -------- Radiobutton пример 1 ----------
# YES_RADIO_STATUS = ('xpath', '//input[@id="yesRadio"]')
# YES_RADIO_ACTION = ('xpath', '//label[@for="yesRadio"]')
# NO_RADIO_STATUS = ('xpath', '//input[@id="noRadio"]')
# NO_RADIO_ACTION = ('xpath', '//label[@for="noRadio"]')
#
# driver.get('https://demoqa.com/radio-button')
# print(driver.find_element(*YES_RADIO_ACTION).is_selected())
# driver.find_element(*YES_RADIO_ACTION).click()
# print(driver.find_element(*YES_RADIO_ACTION).is_selected())


# -------- Radiobutton пример 2 ----------
YES_RADIO_STATUS = ('xpath', '//input[@id="yesRadio"]')
YES_RADIO_ACTION = ('xpath', '//label[@for="yesRadio"]')
NO_RADIO_STATUS = ('xpath', '//input[@id="noRadio"]')
NO_RADIO_ACTION = ('xpath', '//label[@for="noRadio"]')

driver.get('https://demoqa.com/radio-button')
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
