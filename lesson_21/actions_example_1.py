from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

MENU_ITEM_2 = ('xpath', '//a[text()="Main Item 2"]')
SUB_LIST_MENU_ITEM_2 = ('xpath', '//a[text()="SUB SUB LIST »"]')

driver.get('https://demoqa.com/menu')

menu_item_2 = driver.find_element(*MENU_ITEM_2)
sub_list_menu = driver.find_element(*SUB_LIST_MENU_ITEM_2)

action.move_to_element(menu_item_2) \
    .pause(2) \
    .move_to_element(sub_list_menu) \
    .perform()
