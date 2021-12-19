from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from Pages_for_task.register import register
from Pages_for_task.courses import AllCourses

driver = webdriver.Chrome()
driver.implicitly_wait(3)

main_steps = register(driver)
for_courses = AllCourses(driver)

driver.get('https://courses.letskodeit.com/register')
driver.maximize_window()

main_steps.register_steps()
for_courses.nav_to_courses()
for_courses.search_in_courses()
for_courses.results()