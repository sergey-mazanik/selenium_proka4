
# 1. Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
# 2. После каждого клика возвращаться на стартовую страницу.

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://the-internet.herokuapp.com/status_codes')

status_code_links = driver.find_elements('xpath', '//ul/li/a')

for i in range(len(status_code_links)):
    status_code_links[i].click()
    sleep(1)
    driver.back()
