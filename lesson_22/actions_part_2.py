from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

COLUMN_A = ('xpath', '//div[@id="column-a"]')
COLUMN_B = ('xpath', '//div[@id="column-b"]')

driver.get('https://the-internet.herokuapp.com/drag_and_drop')

A = driver.find_element(*COLUMN_A)
B = driver.find_element(*COLUMN_B)

action.drag_and_drop(A, B).perform()