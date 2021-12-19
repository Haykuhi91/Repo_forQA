from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.6pm.com/")
driver.maximize_window()
driver.implicitly_wait(10)
for_shoes = driver.find_element(By.CSS_SELECTOR,"div#root div.dw-z>ul>li>a").click()
#filter
for_woman = driver.find_element(By.CSS_SELECTOR,'div.Fc-z>ul.Ic-z>li:first-child>button').click()
for_sneakers = driver.find_element(By.CSS_SELECTOR,'div.Fc-z>ul.Ic-z>li:first-child>ul>li:nth-child(3)>a').click()
for_size = driver.find_element(By.CSS_SELECTOR,'section.Jt-z>div:last-child>ul>li:nth-child(4)>a').click()
for_brand = driver.find_element(By.CSS_SELECTOR,'input#Brand').send_keys("New Balance")
select_brand = driver.find_element(By.CSS_SELECTOR,'aside#searchFilters div.ot-z>section:nth-child(6)>div.ut-z>ul>li>a:nth-child(1)').click()
for_item = driver.find_element(By.CSS_SELECTOR,'div#products>article:nth-child(38)').click()
selecting_size = driver.find_element(By.CSS_SELECTOR,'select#pdp-size-select').click()
size_5 = driver.find_element(By.CSS_SELECTOR,'select#pdp-size-select>option[value="109855"]').click()
shop = driver.find_element(By.CSS_SELECTOR,'form#buyBoxForm>div:nth-child(3)>div>div div>button[type="submit"]').click()
view_bag = driver.find_element(By.CSS_SELECTOR,'div.Vx-z>div.Xx-z form>a').click()
