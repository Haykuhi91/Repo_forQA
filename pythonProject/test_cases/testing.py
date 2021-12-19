from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from Wikipedia_page.wiki_fr import  FrenchWiki
from Wikipedia_page.Wiki_main import MainPage

driver = webdriver.Chrome()
driver.implicitly_wait(3)

main_wiki = MainPage(driver)
fr_wiki = FrenchWiki(driver)

driver.get('https://www.wikipedia.org/')
driver.maximize_window()

main_wiki.navigate_to_french()
main_wiki.swich_to_another_windows()

fr_wiki.search_tool()
fr_wiki.open_article()


assert driver.find_element(By.XPATH,'//*[@id="firstHeading"]').text == 'Monte Melkonian1', 'title should be Monte Melkonian1'




