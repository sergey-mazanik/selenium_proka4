from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# ------------ Example 1 ------------
# driver.get("https://demoqa.com/sortable")
#
# SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
# TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")
#
#
# def drag_and_drop(source, target):
#     def_source = driver.find_element(*source)  # Находим source-элемент
#     def_target = driver.find_element(*target)  # Находим target-элемент
#     wait.until(EC.element_to_be_clickable(def_source))  # Ждем кликабельности source-элемента
#     action.drag_and_drop(def_source, def_target).perform()  # Перетаскиваем
#
#
# drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR)  # Использование функции


# ------------ Example 2 ------------
driver.get('https://tympanus.net/Development/DragDropInteractions/sidebar.html')

GRID_ITEM = ('xpath', '(//div[@class="grid__item"])[3]')
SIDEBAR_ITEM = ('xpath', '(//div[@class="drop-area__item"])[3]')

action.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .perform()
