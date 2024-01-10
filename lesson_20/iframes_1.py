from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)

FROM_NAME_FIELD_LOCATOR = ('xpath', '//input[@id="RESULT_TextField-0"]')
COPY_TEXT_LOCATOR = ('xpath', '//button[text()="Copy Text"]')
IFRAME_LOCATOR = ('xpath', '//iframe')

driver.get('https://testautomationpractice.blogspot.com')

# driver.switch_to.frame('frame-one796456169')  # переключение по id iframe

iframe = driver.find_element(*IFRAME_LOCATOR)
driver.switch_to.frame(iframe)  # переключение по локатору

driver.find_element(*FROM_NAME_FIELD_LOCATOR).send_keys('Sergey')

driver.switch_to.default_content()  # переключение обратно на страницу

driver.find_element(*COPY_TEXT_LOCATOR).click()
