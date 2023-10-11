from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https:/google.com')
time.sleep(3)
print('strona: ', driver.title)
button1_accept = driver.find_element(by='id', value='L2AGLb')
# print(button1_accept)
# print(type)
button1_accept.click()
time.sleep(2)
# kod z linijek od 8 do 11 można zapisać w jednej linijce:
# driver.find_element(by='id', value='L2AGLb').click()
search_field = driver.find_element(by='name', value='q')
search_field.send_keys('Czy kot ma pepek?')

search_button = driver.find_element(by='name', value="btnK")
search_button.submit()

time.sleep(1)
driver.quit()