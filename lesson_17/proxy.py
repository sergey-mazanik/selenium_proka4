from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = '37.19.220.129:8443'  # proxy server without auth
PROXY_SERVER_AUTH = 'username:password@37.19.220.129:8443'  # proxy server with auth

options = Options()
options.add_argument(f'--proxy-server={PROXY_SERVER}')

driver = webdriver.Chrome(options=options)

driver.get('http://2ip.ru')  # 79.184.19.109
