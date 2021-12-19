import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AllCourses():
    xpath_courses = '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a'
    search_xpath = '//*[@id="search" and @name="course"]'
    search_text = 'selenium'



    def __init__(self, driver):
        self.driver = driver

    def nav_to_courses(self):
        courses = self.driver.find_element(By.XPATH, self.xpath_courses)
        courses.click()
        time.sleep(3)

    def search_in_courses(self):
        search_field = self.driver.find_element(By.XPATH,self.search_xpath)
        search_field.send_keys(self.search_text)
        search_field.send_keys(Keys.ENTER)
        time.sleep(3)

    def results(self):

        for i in range(1,4):
            title = self.driver.find_element(By.XPATH, f'//*[@id="course-list"]/div[{i}]/div/a/div[2]/h4').text
            price = self.driver.find_element(By.XPATH,f'//*[@id="course-list"]/div[{i}]/div/a/div[1]/div[2]/div/span[2]').text
            print(title +" " +price)

