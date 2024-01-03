import os
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')

upload_file_field = driver.find_element('xpath', '//input[@type="file"]')
upload_file_field.send_keys(f'{os.getcwd()}/downloads/person.png')

sleep(3)
