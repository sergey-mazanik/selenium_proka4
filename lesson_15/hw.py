"""Сайт для выполнения задания: https://demoqa.com/selectable

Открыть вкладку Grid
Кликнуть на пару любых элементов
Убедиться, что они выбраны
Кликнуть еще раз и убедиться, что теперь они не выбраны"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

GRID_TAB = ('xpath', '//a[@id="demo-tab-grid"]')
ELEMENT_ONE = ('xpath', '//li[text()="One"]')
ELEMENT_NINE = ('xpath', '//li[text()="Nine"]')

driver.get('https://demoqa.com/selectable')
go_to_grid_tab = driver.find_element(*GRID_TAB)
go_to_grid_tab.click()

select_first_element = driver.find_element(*ELEMENT_ONE)
select_first_element.click()
assert 'active' in driver.find_element(*ELEMENT_ONE).get_attribute('class')

select_second_element = driver.find_element(*ELEMENT_NINE)
select_second_element.click()
assert 'active' in driver.find_element(*ELEMENT_NINE).get_attribute('class')

select_first_element_again = driver.find_element(*ELEMENT_ONE)
select_first_element_again.click()
assert 'active' not in driver.find_element(*ELEMENT_ONE).get_attribute('class')

select_second_element_again = driver.find_element(*ELEMENT_NINE)
select_second_element_again.click()
assert 'active' not in driver.find_element(*ELEMENT_NINE).get_attribute('class')

sleep(1)





