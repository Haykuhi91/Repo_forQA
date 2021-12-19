from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.6pm.com/")
driver.maximize_window()
for_shoes = driver.find_element(By.XPATH,'//div[@class="Lp-z"]/a').click()
#filter
# for_woman = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/div/ul[2]/li[1]/button').click()
# for_sneakers = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/div/ul[2]/li[1]/ul/li[3]/a').click()
# time.sleep(5)
# for_size = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/main/div/div/div/div[6]/aside/div[1]/div[2]/section[2]/div[2]/ul/li[4]/a').click()
# for_brand = driver.find_element(By.XPATH,'//*[@id="Brand"]').send_keys("Jessica Simpson")
# time.sleep(2)
# select_brand = driver.find_element(By.XPATH,'//*[@id="searchFilters"]/div[1]/div[2]/section[4]/div[2]/ul/li/a').click()
# time.sleep(3)
# for_item = driver.find_element(By.XPATH,'//*[@id="products"]/article[4]/a').click()
# time.sleep(3)
# selecting_size = driver.find_element(By.XPATH,'//*[@id="pdp-size-select"]').click()
# time.sleep(2)
# size_5 = driver.find_element(By.XPATH,'//*[@id="pdp-size-select"]/option[2]').click()
# shop = driver.find_element(By.XPATH,'//*[@id="buyBoxForm"]/div[3]/div/div/div/button').click()
# time.sleep(3)
# view_bag = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[3]/form/a').click()