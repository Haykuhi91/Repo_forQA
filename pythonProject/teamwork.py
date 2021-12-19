from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select




driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("https://courses.letskodeit.com/practice%E2%80%8B")
driver.maximize_window()

alert_obj = driver.find_element(By.XPATH,"//*[@id='alertbtn']").click()
alert_obj = driver.switch_to.alert
time.sleep(1)
#print(alert_obj.text())
alert_obj.accept()


alert_confirm = driver.find_element(By.XPATH,"//*[@id='confirmbtn']").click()
time.sleep(1)
alert_confirm = driver.switch_to.alert
time.sleep(1)
alert_obj.dismiss()


hover = driver.find_element(By.XPATH,'//*[@id = "mousehover"]')
actions = ActionChains(driver)
actions.move_to_element(hover)
actions.perform()
for_click = driver.find_element(By.XPATH,"//*[@class='mouse-hover-content']/a[2]")

driver.switch_to.frame('iframe-name')
driver.find_element(By.XPATH, "//*[@class='zen-course-thumbnail']").click()
driver.switch_to.default_content()
simple = driver.find_element(By.XPATH, '//*[@id="alertbtn"]')
simple.click()
time.sleep(3)

alerts = driver.switch_to.alert
print(alerts.text)
alerts.accept()

time.sleep(5)




