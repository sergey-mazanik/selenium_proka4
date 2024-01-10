from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_CLICK_BUTTON = ('xpath', '//button[@name="leftClick"]')  # левая кнопка мыши
DOUBLE_CLICK_BUTTON = ('xpath', '//button[@name="doubleClick"]')  # дабл клик
CONTEXT_CLICK_BUTTON = ('xpath', '//button[@name="rightClick"]')  # Правая кнопка мыши
COLOR_CHANGE_BUTTON = ('xpath', '//button[@name="colorChangeOnHover"]')  # Кнопка, изменяющая цвет при наведении

driver.get('https://testkru.com/Elements/Buttons')

left_button = driver.find_element(*LEFT_CLICK_BUTTON)
# action.click(left_button).perform()
#
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON)
# action.double_click(double_button).perform()
#
context_button = driver.find_element(*CONTEXT_CLICK_BUTTON)
# action.context_click(context_button).perform()

color_change_button = driver.find_element(COLOR_CHANGE_BUTTON)

# action.click(left_button) \
#     .pause(2) \
#     .double_click(double_button) \
#     .pause(2) \
#     .context_click(context_button) \
#     .perform()

action.move_to_element(color_change_button) \
    .perform()
