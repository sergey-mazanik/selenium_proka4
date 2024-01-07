from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# --------- Использование клавиатуры ---------
# KEYBOARD_INPUT = ('xpath', '//input[@id="target"]')
#
# driver.get('https://the-internet.herokuapp.com/key_presses')
#
# driver.find_element(*KEYBOARD_INPUT).send_keys("isdhfksdSDKH")
# sleep(1)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.COMMAND + 'A')
# sleep(1)
# driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
# sleep(1)

# --------- Современный дропдаун 1 ---------
# SELECT_LOCATOR = ('xpath', '//input[@id="react-select-3-input"]')
# driver.get('https://demoqa.com/select-menu')

# driver.find_element(*SELECT_LOCATOR).send_keys('Ms.')
# driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)


# --------- Современный дропдаун 2 ---------
# SELECT_ONE = ('xpath', '//div[@id="selectOne"]')
# PROF_OPTION = ('xpath', '//div[text()="Prof."]')
# driver.get('https://demoqa.com/select-menu')
# driver.find_element(*SELECT_ONE).click()
# driver.find_element(*PROF_OPTION).click()


# --------- Мультиселект ---------
# MULTISELECT_LOCATOR = ('xpath', '//input[@id="react-select-4-input"]')
# driver.get('https://demoqa.com/select-menu')
#
# driver.find_element(*MULTISELECT_LOCATOR).send_keys('Gre')
# driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
