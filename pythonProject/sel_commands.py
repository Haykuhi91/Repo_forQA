from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select




driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
for_english = driver.find_element(By.XPATH,'//*[@id="js-link-box-en"]').click()
print(driver.current_url)
driver.back()
print(driver.window_handles)

driver.execute_script("window.open('https://en.wikipedia.org/wiki/Main_Page');")
driver.switch_to.window(driver.window_handles[0])
for_russian = driver.find_element(By.XPATH,'//*[@id="js-link-box-ru"]').click()
link = driver.current_url
driver.execute_script("window.open('link')")
driver.back()
driver.find_element(By.XPATH,'//*[@id="js-link-box-fr"]').click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    search = driver.find_element(By.XPATH,'//*[@id="searchInput"]')
    search.send_keys("Monte Melkonian")
    search.send_keys(Keys.ENTER)

driver.switch_to.window(driver.window_handles[0])

var_list = driver.find_elements(By.XPATH,'//*[@id="p-Contribuer"]/div/ul/li/a')
print(var_list)
for i in var_list:
    actions = ActionChains(driver)
    actions.move_to_element(i)
    actions.perform()
    time.sleep(2)





