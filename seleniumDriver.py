from selenium import webdriver
import time

driver1 = webdriver.Chrome()  # klik w Chroma z lewym CTRL; pod nazwą driver mam moje okno; ten zapis mówi stwórz okienko
driver1.get('https:/google.com')
time.sleep(1)

driver2 = webdriver.Chrome()  # klik w Chroma z lewym CTRL; pod nazwą driver mam moje okno; ten zapis mówi stwórz okienko
driver2.get('https:/allegro.pl')
time.sleep(1)

driver3 = webdriver.Chrome()  # klik w Chroma z lewym CTRL; pod nazwą driver mam moje okno; ten zapis mówi stwórz okienko
driver3.get('https:/wp.pl')
time.sleep(1)

driver1.quit()
driver2.quit()
driver3.quit()