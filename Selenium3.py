from selenium import webdriver
from Selenium3class import LoginPage
from Selenium2 import make_screenshot
import time
import pytest

@pytest.mark.parametrize('username', ['standard_user', 'lockout_user'])
def test_lgin_page(username):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username) # parametr
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
