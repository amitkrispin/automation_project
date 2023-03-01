from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from home_page_AOS import Advantge_page
from items_in_cart import Items_In_Cart
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
service_chrome = Service(r"C:\selenum1\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.implicitly_wait(10)
advantge=Advantge_page(driver)
cart=Items_In_Cart(driver)
advantge.user_button().click()
advantge.username().send_keys("project")
advantge.password().send_keys("1234Qwer")
advantge.signIN_button().click()
sleep(2)
driver.find_element(By.ID,"menuCart").click()
print(cart.items_title())



sleep(3)