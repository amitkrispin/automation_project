from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class Items_In_Cart:
    def __init__(self, driver: webdriver.Chrome) :
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    def tablte_cart(self):
        return self.driver.find_element(By.CLASS_NAME,"fixedTableEdgeCompatibility")
    def table_rows(self):
        return self.tablte_cart().find_elements(By.TAG_NAME,"tr")
    def items_title(self):
        return self.table_rows()[1].find_elements(By.TAG_NAME,"td")
    def item_title_for(self):
        for row in self.items_title():
            return row.text