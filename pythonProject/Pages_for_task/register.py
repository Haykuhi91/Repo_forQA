from selenium.webdriver.common.by import By
import random


class register():

    firstname_xpath = '//*[@id="name"]'
    firstname_text = 'Haykuhi'
    lastname_xpath = '//*[@id="last_name"]'
    lastname_text = 'Hakobyan'
    email_xpath = '//*[@id="email"]'
    email_text =  str(random.randrange(1,100)) + 'hak@gmail.com'
    password_xpath = '//*[@id="password"]'
    password2_xpath = '//*[@id="password_confirmation"]'
    pass_text = 'qwert111'
    signup_xpath = '//*[@id="page"]/div[2]/div/div/div/div/form/div[7]/div[1]/input'


    def __init__(self,driver):
        self.driver = driver

    def register_steps(self):
        self.driver.find_element(By.XPATH,self.firstname_xpath).send_keys(self.firstname_text)
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(self.lastname_text)
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(self.email_text)
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(self.pass_text)
        self.driver.find_element(By.XPATH, self.password2_xpath).send_keys(self.pass_text)
        self.driver.find_element(By.XPATH,self.signup_xpath).click()

