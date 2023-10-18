from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https:/google.com')
time.sleep(1)
print('strona: ', driver.title)

button1_accept = driver.find_element(by='id', value='L2AGLb')
# print(button1_accept)
# print(type)
button1_accept.click()
time.sleep(1)
# driver.find_element(by='id', value='L2AGLb').click() <-- kod z linijek od 8 do 11 można zapisać w jednej linijce:
search_field = driver.find_element(by='name', value='q')
search_field.send_keys('Dokąd nocą tupta jeż??')
# search_field = driver.find_element(by='name', value="btnK")
# search_button.submit()
search_field.send_keys(Keys.ENTER)
driver.get_screenshot_as_file('_zrzut_ekranu.png')


time.sleep(1)
driver.quit()