from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import  TimeoutException
from selenium2 import make_screenshot



def czekaj_na_id(element_id):
    timeout = 3
    timeout_message = f"Element o ID {element_id} nie pojawił się w czasie {timeout} s."
    lokalizator = (By.ID, element_id)
    znaleziono = excon.visibility_of_element_located(lokalizator)  # sprawdzamy, czy element jest
    oczekiwator = WebDriverWait(driver, timeout) # jak długo czekać i gdzie
    return oczekiwator.until(method=znaleziono, message=timeout_message)

#excon.visibility_of_element_located(lokalizator)

def make_screenshot(okno_przegladarki):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen' + short_date + '.png'
    okno_przegladarki.get_screenshot_as_file(screen_name)


driver = webdriver.Chrome()
driver.maximize_window()    # przejście na pełny ekran
driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)

try:
    login_button = czekaj_na_id('login-button')
except TimeoutException:
    print('Nie znaleziono')
    raise
else:
    print('Znaleziono')
finally:
    print('xxx')
    make_screenshot(driver)
    driver.quit()

try:
    username_field = driver.find_element('id','user-name2')
except:
    print('nie znaleziono, szukam standardowych credentiali')
    username_field = driver.find_element('id', 'user-name')
    make_screenshot(driver)

time.sleep(1)
username_field.clear()
username_field.send_keys('standard_user')

try:
    password_field = driver.find_element('id','user-name') # jeśli nie znajdziemy żadnego id i name, możeny poszukać po xpath:
except NoSuchElementException:   # można wpisać, jakiś konkretny błąd, albo z dostępnych lub zaimportować dodatkowo z selenium                                                 # by: 'xpath', value: '//*[@id="password"]'
    make_screenshot(driver)
    print('nie znaleziono pola z hasłem')
    raise

password_field.send_keys('secret_sauce')

login_button = driver.find_element('name', 'login-button')
if not login_button.get_attribute('disabled'):  # czy przycisk aktywny
    login_button.click()

driver.get_screenshot_as_file('screen.png')

make_screenshot(driver)

driver.quit()

'''
z tego zrobiliśmy funkcję make_screenshot:
today = datetime.datetime.today()
short_date = today.strftime('_stamp%H%M%S')
screen_name = 'screen' + short_date + '.png'
driver.get_screenshot_as_file(screen_name)
'''


