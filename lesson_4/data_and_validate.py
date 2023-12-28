# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get('http://www.wikipedia.org/')
#
# url = driver.current_url  # отображение текущего урл
# print(f'URL page: {url}')
# assert url == 'http://www.wikipedia.org/', 'not correct url'
#
# current_title = driver.title  # отображение текущего тайтла страницы
# print(f'Current title: {current_title}')
# assert current_title == 'Wikipedia', 'not correct title'
#
# PAGE_SOURCE = driver.page_source  # отображение всего HTML страницы




# driver.get('http://google.com/')
# url_goo = driver.current_url
# print(url_goo)
#
# driver.get('http://ya.ru/')
# url_ya = driver.current_url
# print(url_ya)
#
# driver.back()
# assert driver.current_url == url_goo
#
# driver.refresh()
# current_url = driver.current_url
# print(current_url)
#
# driver.forward()
# assert driver.current_url == url_ya
# print('OK!')

