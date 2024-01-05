import os
from time import sleep
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://5element.by/')

ADD_TO_BASKET = ('xpath', '//button[@data-product_id="792176"]')

driver.execute_script('window.scrollBy(0, 1200);')
add_product = wait.until(EC.element_to_be_clickable(ADD_TO_BASKET)).click()
pickle.dump(driver.get_cookies(), open(os.getcwd() + '/cookies/cookies_5el.pkl', 'wb'))

driver.delete_all_cookies()
print(driver.get_cookies())

sleep(3)

cookies = pickle.load(open(os.getcwd()+'/cookies/cookies_5el.pkl', 'rb'))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
print(driver.get_cookies())

sleep(3)
