import os
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--headless')
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option('prefs', prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/download')
sleep(2)
elements = driver.find_elements('xpath', '//a')
elements[2].click()
sleep(2)
