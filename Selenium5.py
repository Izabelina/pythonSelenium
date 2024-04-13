from selenium import webdriver
from Selenium3class import LoginPage
from Selenium2 import make_screenshot
import time
import pytest

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=nasze_options)
driver.maximize_window()
driver.get('http://allegro.pl')
time.sleep(1)
driver.quit()

# przejscie do drugiej karty
currentWindowName = driver.current_window_handle
windowNames = driver.window_handles # nazwy wszystkich kart
# print(windowNames)

for okno in windowNames:
    if okno != currentWindowName:
        driver.switch_to.window(okno)

