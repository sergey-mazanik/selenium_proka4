from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/en/us/login')

driver.add_cookie({
    "name": "username",
    "value": "user123"
})

driver.refresh()

print(driver.get_cookie('username'))
