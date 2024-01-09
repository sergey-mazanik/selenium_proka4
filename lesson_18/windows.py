from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options)


# FOR_BUSINESS_BUTTON_LOCATOR = ('xpath', '//a[text()=" For Business "]')
# START_FREE_BUTTON_LOCATOR = ('xpath', '//a[text()="Start for Free"]')

# driver.switch_to.new_window('tab')  # Открытие браузера + открытие новой вкладки и переключение на нее
# driver.switch_to.new_window('window')  # Открытие браузера + открытие нового окна и переключение на него
# driver.get('https://hyperskill.org/tracks')

# print(driver.current_window_handle)  # вывод дескриптора открытой вкладки/окна
# print(driver.window_handles)  # вывод списка дескрипторов всех открытых вкладок/окон

# ------- Переключение между вкладками -------
# driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])
#
# driver.find_element(*START_FREE_BUTTON_LOCATOR).click()


# ------- Открытие нового окна -------
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# driver.get('https://ya.ru')

# driver.quit() # Закрытие сессии, т.е всего браузера
# driver.close() # Закрытие активного окна / вкладки


# ------- Пример -------
# # Шаг 1 - Открыть базовую страницу
# driver.get("https://whatismyipaddress.com/")
# # Шаг 2 - Получение дескриптора текущего окна
# old_window = driver.current_window_handle
# print("Дескриптор первого окна: ", old_window)
# # Шаг 3 - Открытие и переключение на новое окно
# driver.switch_to.new_window("window")
# # Шаг 4 - Получение дескриптора нового окна
# new_window = driver.current_window_handle
# print("Дескриптор второго окна: ", new_window)
# # Шаг 5 - Проверка, что окно переключилось
# assert new_window == driver.current_window_handle, "Окно не переключилось"
# sleep(2)
# # Шаг 6 - Открытие страницы в новом окне
# driver.get("https://vk.com")
# # Шаг 7 - Переключение на старое окно
# driver.switch_to.window(old_window)
# # Шаг 8 - Проверка, что переключились на старое окно
# assert old_window == driver.current_window_handle, "Окно не переключилось"
# # Шаг 9 - Открытие страницы в старом окне
# driver.get("https://ya.ru")
# # Шаг 10 - Переключение на новое окно
# driver.switch_to.window(new_window)
# # Шаг 11 - Закрытие нового окна
# driver.close()
