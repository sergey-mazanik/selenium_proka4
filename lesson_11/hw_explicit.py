from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

# Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом
CHANGE_TEXT_BUTTON = ('xpath', '//button[@id="populate-text"]')
TEXT_FIELD = ('xpath', '//h2[@id="h2"]')

click_change_text_button = wait.until(EC.element_to_be_clickable(CHANGE_TEXT_BUTTON))
click_change_text_button.click()
text_field = wait.until(EC.text_to_be_present_in_element(TEXT_FIELD, 'Selenium Webdriver'))
print('1 - OK')

# Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”
DISPLAY_BUTTON = ('xpath', '//button[@id="display-other-button"]')
HIDDEN_BUTTON = ('xpath', '//button[@id="hidden"]')

display_button_after_10_sec = wait.until(EC.element_to_be_clickable(DISPLAY_BUTTON))
display_button_after_10_sec.click()
enabled_button = wait.until(EC.text_to_be_present_in_element(HIDDEN_BUTTON, 'Enabled'))
print('2 - OK')

# Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”
ENABLE_BUTTON = ('xpath', '//button[@id="enable-button"]')
DISABLE_BUTTON = ('xpath', '//button[@id="disable"]')

click_enable_button = wait.until(EC.element_to_be_clickable(ENABLE_BUTTON))
click_enable_button.click()
disable_button = wait.until(EC.element_to_be_clickable(DISABLE_BUTTON))
print('3 - OK')

# Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта
OPEN_ALERT_BUTTON = ('xpath', '//button[@id="alert"]')

open_alert_button = wait.until(EC.element_to_be_clickable(OPEN_ALERT_BUTTON))
open_alert_button.click()
alert = wait.until(EC.alert_is_present())
print('4 - OK')
