import time

from selenium import webdriver
from Selenium3class import LoginPage
from Selenium2 import make_screenshot

driver = webdriver.Chrome()
# driver.maximize_window() tu robię to ręcznie, jeśli nie chcę rbic recznie, trzeba wrzucic to do klasy

page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')
page.click_login()
time.sleep(3)

try:
    assert driver.current_url == 'https://www.saucedemo.com/investory.html', make_screenshot(driver)
except AssertionError:
    print('blad, zly adres')
    raise
else:
    print('ok, dobry adres')
finally:
    driver.quit()


driver.quit()
