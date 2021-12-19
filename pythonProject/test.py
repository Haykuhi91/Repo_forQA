from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import random

# driver = webdriver.Chrome()
# driver.implicitly_wait(7)
# driver.get("https://practice.automationbyte.com/forms/basic-form-1.php")
# driver.maximize_window()

mail = str(random.randrange(1,100)) + 'hak@gmail.com'
print(mail)


# go_to_home = driver.find_element(By.XPATH,"//a[text()='Home ']").click()
#
# #driver.back()
# #or
# driver.execute_script("window.history.go(-1)")
#
# driver.refresh()
# first_name = driver.find_element(By.XPATH,"//input[@name='firstNameInput']").send_keys("Haykuhi")
# last_name = driver.find_element(By.XPATH,"//input[@name='lastNameInput']").send_keys("Hakobyan")
# gender = driver.find_element(By.XPATH,"//input[@value='Female']").click()
# text_for_input = driver.find_element(By.XPATH,"//p[@class='text-muted text-center']").text
# add_info = driver.find_element(By.XPATH,'//textarea').send_keys(text_for_input)
# for_hobbies = driver.find_element(By.XPATH,"//div[@class='checkbox'][4]//input").click()
# select_country = Select(driver.find_element(By.XPATH,"//select[@id='countryInput']"))
# select_country.select_by_visible_text("Canada")
# register = driver.find_element(By.XPATH,"//button[text()='Register']").click()
# reset = driver.find_element(By.XPATH,'//button[text()="Reset"]').click()
#
#
#
#
#
