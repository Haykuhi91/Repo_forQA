from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://staff.am/")
print(driver.title)
search_bar = driver.find_element("name","TrainingsFilter[key_word]")
search_bar.send_keys("quality assurance", Keys.ARROW_DOWN)
time.sleep(3)
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
print(driver.current_url)
driver.close()