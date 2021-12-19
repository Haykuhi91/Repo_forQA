from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
navigate_tool = driver.find_element(By.ID,"nav-hamburger-menu")
navigate_tool.click()
nav_close = driver.find_element("id","hmenu-canvas-background")
nav_close.click()
orders_tool = driver.find_element("id","nav-orders")
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("Vitamin D")
search_bar.send_keys(Keys.ENTER)

