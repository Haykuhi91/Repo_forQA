from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.6pm.com/")
driver.maximize_window()
driver.implicitly_wait(10)
for_shoes = driver.find_element(By.XPATH,'//div[@class="dw-z"]//a[text()="Shoes"]').click()
#filter
for_woman = driver.find_element(By.XPATH,'//ul[@class="Xd-z"]/descendant::button').click()
for_sneakers = driver.find_element(By.XPATH,'//a[text()="Sneakers & Athletic"]').click()
for_size = driver.find_element(By.XPATH,"//div[@class='FA-z']//span[text()='5']").click()
for_brand = driver.find_element(By.XPATH,'//*[contains(@id,"brand")]/following-sibling::div/child::form/child::input').send_keys("New Balance")
select_brand = driver.find_element(By.XPATH,'//div[@class="FA-z"]//span[text()="New Balance"]/parent::a').click()
for_item = driver.find_element(By.XPATH,'//div[@id="products"]//a[text()="New Balance - 510v5. Color Natural Indigo/Nb Light Blue. Low Stock."]').click()
selecting_size = Select(driver.find_element(By.XPATH,'//select[@id="pdp-size-select"]'))
selecting_size.select_by_visible_text("5")
selecting_width = Select(driver.find_element(By.XPATH,'//select[@id="pdp-width-select"]'))
selecting_width.select_by_value("110335")
shop = driver.find_element(By.XPATH,'//div[@class="IE-z"]/button[@type="submit"]').click()
view_bag = driver.find_element(By.XPATH,'//a[@class="uK-z"]').click()