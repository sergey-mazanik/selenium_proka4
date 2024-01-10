from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from lesson_23.scrolls import Scrolls


driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get('https://seiyria.com/bootstrap-slider/')

EX_2_LOCATOR = ('xpath', '//h3[text()="Example 2: "]')
ex_2 = driver.find_element(*EX_2_LOCATOR)

# action.scroll_to_element(ex_2).perform()  # скролл к элементу цепочкой действий (элемент отображается внизу страницы)

scrolls.scroll_to_element(ex_2)

sleep(2)
