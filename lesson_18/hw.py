from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

RESET_PASSWORD = ('xpath', '//a[text()=" Reset password "]')  # for hyperskill
PLACE_AN_AD = ('xpath', '(//button[@type="button"])[1]')  # for av
BASKET = ('xpath', '//span[text()="Корзина"]')  # for ozon

tabs = []
driver.get('https://hyperskill.org/login')
tabs.append(driver.current_window_handle)
driver.switch_to.new_window('tab')
driver.get('https://www.av.by/')
tabs.append(driver.current_window_handle)
driver.switch_to.new_window('tab')
driver.get('https://www.ozon.by/')
tabs.append(driver.current_window_handle)
driver_tabs = driver.window_handles
assert tabs == driver_tabs

driver.switch_to.window(tabs[0])
print(f'Title for the first tab is "{driver.title}"')
driver.find_element(*RESET_PASSWORD).click()
print(f'URL for first tab is "{driver.current_url}"')

print('-' * 10)

driver.switch_to.window(tabs[1])
print(f'Title for the second tab is "{driver.title}"')
driver.find_element(*PLACE_AN_AD).click()
print(f'URL for second tab is "{driver.current_url}"')

print('-' * 10)

driver.switch_to.window(tabs[2])
print(f'Title for the third tab is "{driver.title}"')
driver.find_element(*BASKET).click()
print(f'URL for third tab is "{driver.current_url}"')

driver.quit()
