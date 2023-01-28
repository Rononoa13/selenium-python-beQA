from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilibox import Toolbox
import time

class TestlandingPage(Toolbox):
    
    def test_landing_page(self):
        self.url()
        brand_text = self.driver.find_element(By.CSS_SELECTOR, "a.brand").text
        assert brand_text == 'Zero Bank'

    def test_searchbox(self):
        search_term = self.driver.find_element(By.ID, 'searchTerm')
        search_term.send_keys('faketext')
        search_term.send_keys(Keys.ENTER)
        assert self.driver.find_element(By.CSS_SELECTOR, '.top_offset > h2').text == "Search Results:"