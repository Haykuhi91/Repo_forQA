import time

from selenium.webdriver.common.by import By


class FrenchWiki():
    xpath_search = '//*[@id="searchInput"]'
    input_text = 'Monte Meklonian'
    xpath_for_MM = '//*[@id="mw-content-text"]/div[5]/ul/li[1]/div[1]/a'
    for_list = '//*[@id="mw-content-text"]/div[5]/ul//a'



    def __init__(self, driver):
        self.driver = driver

    def search_tool(self):
        search_field = self.driver.find_element(By.XPATH, self.xpath_search)
        search_field.send_keys(self.input_text)
        search_field.submit()
        time.sleep(3)

    # def open_article(self):
        # mylist = self.driver.find_elements(By.XPATH, self.for_list)
        # print(mylist)
        # for item in mylist:
        #     # article = self.driver.find_element(f(By.XPATH,{item}))
        #     item.click()
        #     self.driver.back()
        #     time.sleep(3)
        # # for_open = self.driver.find_element(By.XPATH,self.xpath_for_MM).click()


    def open_article(self):
        list_for_search = self.driver.find_elements(By.XPATH, self.for_list)
        print(list_for_search)
        for x in list_for_search:
            self.driver.find_element(By.XPATH,x).click()
            self.driver.back()
            time.sleep(3)




