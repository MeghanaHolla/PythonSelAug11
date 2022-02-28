import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_link_text("JavaScript Alerts").click()

driver.find_element_by_css_selector("#content > div > ul > li:nth-child(1) > button").click()

time.sleep(5)

driver.switch_to.alert.accept()