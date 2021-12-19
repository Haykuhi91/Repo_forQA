from selenium.webdriver.common.by import By


class MainPage():

    french_xpath = '//*[@id="js-link-box-fr"]'

    def __init__(self,driver):
        self.driver = driver

    def navigate_to_french(self):
        self.driver.find_element(By.XPATH,self.french_xpath).click()

    def swich_to_another_windows(self):
        self.driver.execute_script("window.open('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal')")
        self.driver.switch_to.window(self.driver.window_handles[1])



