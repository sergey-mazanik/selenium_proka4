from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('http://yandex.ru')
sleep(2)

driver.back()  # возврат на предыдущую страницу браузера
driver.forward()  # переход на следующую страницу браузера
driver.refresh()  # перезагрузка страницы
